import discord
import time
from replit import db

from tools import getBal,getAccountInfo,canClaimDaily,dailyReward,DailyclaimTimeleft,claimDaily_,delAccount,transferMoney,checkHasAccount,getAccountsData,updateData,setMoney,addMoney,enableDailyReminder,disableDailyReminder,updateName_,getTime

from settings import bc_cmds,db_format,lb_default,uDontHaveAcc,couldNotAddMoney,accDoesNotExist,forgotMention,improperData_msg,couldNotSetMoney,errorOccured,invalidAmount,accAlreadtCreatedFor,accCreatedFor,updateSuccess,unknownError,reminderSet,reminderRemoved,notReminderSet,notReminderRemoved,infoUpdateSuccess,infoUpdateFail,couldNotGetDB,couldNotDelete,one_day


async def bcExecuteCommand(message, command, op):
    for cmd in bc_cmds["balance"]:
        if command[0] == cmd:
            await showBalance(message, command, op)
    for cmd in bc_cmds["setbalance"]:
        if command[0] == cmd:
            await setBalance(message, command, op)
    for cmd in bc_cmds["addbalance"]:
        if command[0] == cmd:
            await addBalance(message, command, op)
    for cmd in bc_cmds["transfer"]:
        if command[0] == cmd:
            await transfer(message, command, op)
    for cmd in bc_cmds["create"]:
        if command[0] == cmd:
            await create(message, command, op)
    for cmd in bc_cmds["leaderboard"]:
        if command[0] == cmd:
            await showLeaderboard(message, command, op)
    for cmd in bc_cmds["delete"]:
        if command[0] == cmd:
            await delete(message, command, op)
    for cmd in bc_cmds["deleteall"]:
        if command[0] == cmd:
            await deleteAll(message, command, op)
    for cmd in bc_cmds["daily"]:
        if command[0] == cmd:
            await claimDaily(message, command, op)
    for cmd in bc_cmds["update"]:
        if command[0] == cmd:
            await update(message, command, op)
    for cmd in bc_cmds["reminddaily"]:
        if command[0] == cmd:
            await remindDaily(message, command, op)
    for cmd in bc_cmds["updatename"]:
        if command[0] == cmd:
            await updateName(message, command, op)
    for cmd in bc_cmds["getdaychange"]:
        if command[0] == cmd:
            await getDayChange(message, command, op)


async def getDayChange(message,command,op):
  #awit message.channel.send("getDayChange")
  try:
    if op:
      lastDayChange = db.get("lastDayChange")
      timeleft_ = (float(lastDayChange)+one_day)-float(time.time())
      timeLeft = getTime(timeleft_)

      msg_Timeleft = ""
      for key in timeLeft.keys():
        temp = timeLeft[key]
        if temp == 0:
          pass
        elif temp == 1:
          msg_Timeleft = msg_Timeleft + f" {temp} {key[0:len(key)-1]}"
        else:
          msg_Timeleft = msg_Timeleft + f" {temp} {key}"

      await message.channel.send(f"Day change in {msg_Timeleft}.")
    else:
      await message.channel.send("You dont have permission to use that")
  except Exception as error:
    await message.channel.send(errorOccured + str(error))


async def updateName(message,command,op):
  #await message.channel.send("update Name") #for testing
  try:
    #Get info to update
    if op: #so op can update for others
      try:
        idC = message.mentions[0].id
        nameC = message.mentions[0].name
        discriminatorC = message.mentions[0].discriminator
      except:
        idC = message.author.id
        nameC = message.author.name
        discriminatorC = message.author.discriminator
    else:
      idC = message.author.id
      nameC = message.author.name
      discriminatorC = message.author.discriminator

    info = getAccountInfo(idC) #get info
    if info == False: #to check info exist/has account
      await message.channel.send(accDoesNotExist) #error
      return
    else:
      if updateName_(idC,nameC,discriminatorC):  #Updates info
        await message.channel.send(infoUpdateSuccess)
      else:
        await message.channel.send(infoUpdateFail)
  except Exception as error:
    await message.channel.send(errorOccured+str(error))

async def remindDaily(message,command,op):
  #await message.channel.send("remindmeDaily") #for testing
  try:
    #get ID
    if op: #so op can change things for others
      try:
        idC = message.mention[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id  #get id to remind
    
    try: #To check if they want to enable or disable the reminder
      if str(command[1]).lower() == "true":
        doRemind = True
      elif str(command[1]).lower() == "false":
        doRemind = False
      else:
        await message.channel.send(improperData_msg) #error
        return
    except:
      await message.channel.send(improperData_msg) #error
      return

    info = getAccountInfo(idC) #get info
    if info == False: #check if has account
      await message.channel.send(accDoesNotExist) #error
      return
    if doRemind:  #enable Daily Reminder
      if enableDailyReminder(idC):
        await message.channel.send(reminderSet)
      else:
        await message.channel.send(notReminderSet)
    else:   #Disable Daily Reminder
      if disableDailyReminder(idC):
        await message.channel.send(reminderRemoved)
      else:
        await message.channel.send(notReminderRemoved)
  except Exception as error:
    await message.channel.send(errorOccured+str(error))



async def claimDaily(message,command,op):
  #await message.channel.send("claim Daily") #For testing

  try:
    #get ID
    if op: #so op can do things for others
      try:
        idC = message.mentions[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id
      
    info = getAccountInfo(idC) #Get info of user to claim

    if info == False:  #if did not find the account of the user
      await message.channel.send(uDontHaveAcc)  #error
      return
    else:
      if canClaimDaily(idC):
        try:
          reward = dailyReward(idC)
        except:
          print("yes here")
        if claimDaily_(idC,reward):
          await message.channel.send(f"Successfully claimed daily reward!! \nConsecutive Login : {info['Loginstreak']}\nReward : {reward}")
        else:
          await message.channel.send(couldNotAddMoney)
      else:
        timeLeft = DailyclaimTimeleft(idC)   #Calculate time left to claim
        msg_Timeleft = ""
        for key in timeLeft.keys():
          temp = timeLeft[key]
          if temp == 0:
            pass
          elif temp == 1:
            msg_Timeleft = msg_Timeleft + f" {temp} {key[0:len(key)-1]}"
          else:
            msg_Timeleft = msg_Timeleft + f" {temp} {key}"

        await message.channel.send(f"Sorry you can not claim.\nYou Need to wait for{msg_Timeleft}.")
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def showBalance(message, command, op):
  #await message.channel.send("Show Balance!!")    #for testing

  #Id of user to claim daily
  try:
    idC = message.mentions[0].id  #if they mentions some one use that id
  except:
    idC = message.author.id

  try:
    info = getAccountInfo(idC) #Get info of user to claim

    if info == False:  #if did not find the account of the user
      await message.channel.send(accDoesNotExist)
      return
    else:
      embed = discord.Embed(title="Balance",color=discord.Color.blue())
      embed.add_field(name=str(info["Name"]),value=":coin: BC "+str(info["Balance"]),inline=False)
      await message.channel.send(embed=embed)     #send info
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def setBalance(message, command, op):
  if op: #so only op can use this command
    #await message.channel.send("set Balance") #For testing
    
    try:
      idC = message.mentions[0].id  #Id of user
    except:
      await message.channel.send(forgotMention) #error
      return
    try:
      moneyToSet = command[1]  #get amount to set
    except:
      await message.channel.send(improperData_msg) #error
      return

    try:
      info = getAccountInfo(idC) #Get info of user to claim

      if info == False:  #if did not find the account of the user
        await message.channel.send(uDontHaveAcc)
        return
      else:
        if setMoney(idC,moneyToSet):
          await message.channel.send(f"Successfully set money to {moneyToSet} for {info['Name']}")
        else:
          await message.channel.send(couldNotSetMoney)
    except Exception as error:
      await message.channel.send(errorOccured+str(error))
  else:
    await message.channel.send("You dont have permission to use that")


async def delete(message, command, op):
    #await message.channel.send("Delete!!")  # for Testing

    #get ID
    if op: #so op can delete others acc
      try:
        id_ = message.mentions[0].id
      except:
        id_ = message.author.id
    else:
      id_ = message.author.id

    try:
      info = getAccountInfo(id_)
      if info != False:
        if delAccount(id_):
          await message.channel.send(f"Successfully deleated {info['Name']}'s account")
        else:
          await message.channel.sent(couldNotDelete)
      else:
        await message.channel.sent(accDoesNotExist)
    except Exception as error:
      await message.channel.send(errorOccured+str(error))


async def deleteAll(message, command, op):
  if op: #so only op can do this
    # for Testing
    #await message.channel.send("Delete All!!")

    try:
      db.set("data",[])
      await message.channel.send("Successfully cleared the database ")
    except Exception as err:
      await message.channel.send("An Error occured sorry " + str(err))
  else:
    await message.channel.send("You dont have permission to use that")


async def addBalance(message, command, op):
  if op: #so only op can use this command
    #await message.channel.send("set Balance") #For testing
    try:
      try:
        idC = message.mentions[0].id  #Id of user
      except:
        await message.channel.send(forgotMention)
        return
      try:
        moneyToAdd = float(command[1])  #money To add to the user
      except:
        await message.channel.send(improperData_msg)
        return

      info = getAccountInfo(idC) #Get info of user to claim

      if info == False:  #if did not find the account of the user
        await message.channel.send(uDontHaveAcc)
        return
      else:
        if addMoney(idC,moneyToAdd):
          await message.channel.send(f"Successfully added :coin: BC {moneyToAdd} to {info['Name']}")
        else:
          await message.channel.send(couldNotAddMoney)
    except Exception as error:
      await message.channel.send(errorOccured+str(error))
  else:
    await message.channel.send("You dont have permission to use that")



async def transfer(message, command, op):
  # for Testing
  #await message.channel.send("Transfer!!")

  #get id of form and to
  if op: #so op can make some one pay
    try:
      id_from = message.mentions[1].id
      id_to = message.mentions[0].id
      name_from = message.mentions[1].name
      name_to = message.mentions[0].name
    except:
      id_from = message.author.id
      id_to = message.mentions[0].id
      name_from = message.author.name
      name_to = message.mentions[0].name
  else:
    id_from = message.author.id
    id_to = message.mentions[0].id
    name_from = message.author.name
    name_to = message.mentions[0].name
  try:
    amount = float(command[1]) #amount to transfer
    if amount <= 0:
      await message.channel.send(invalidAmount) #error
      return
  except:
    await message.channel.send(invalidAmount) #error
    return
  try:
    fromInfo = getAccountInfo(id_from)
    toInfo = getAccountInfo(id_to)
    if transferMoney(id_from,id_to,amount):
      await message.channel.send(f"Amount :coin: {amount} tranfered from {name_from} to {name_to}")
    else:
      if fromInfo == False or toInfo == False:
        await message.channel.send("Sorry could find the Account")
      elif float(fromInfo["Balance"]) <= float(amount):
        await message.channel.send(f"Sorry {name_from} does not have enough money :coin:")
  except Exception as error:
    await message.channel.set(errorOccured+str(error))


async def create(message, command, op):
  #for testing
  #await message.channel.send("Create!!")

  #get info to create
  if op: #so op can create acc for others
    try:
      idC = message.mentions[0].id
      nameC = message.mentions[0].name
      discriminatorC = message.mentions[0].discriminator
    except:
      idC = message.author.id
      nameC = message.author.name
      discriminatorC = message.author.discriminator
  else:
    idC = message.author.id
    nameC = message.author.name
    discriminatorC = message.author.discriminator
  #check if already created
  created = checkHasAccount(idC)

  #if account already Created
  if created:
      await message.channel.send(accAlreadtCreatedFor+nameC) #error
  else:#create accound
    #manage Info
    info = db_format
    info["ID"]=str(idC)
    info["Name"]=str(nameC)
    info["Discriminator"]=str(discriminatorC)
    info["Lastclaimed"]= time.time()

    try:
      #try to get data form database and add the info to database
      data = db.get("data")
      data.append(info)
      db.set("data",data)
      await message.channel.send(accCreatedFor+nameC)
    except Exception as error:
        #if error send error message
        await message.channel.send(errorOccured+error)


async def showLeaderboard(message,command, op):
  #for testing
  #await message.channel.send("Show Leaderboard!!")

  try:
    data = getAccountsData()
    if data == False:
      await message.channel.send(couldNotGetDB)
    else:
      data.sort(key=getBal,reverse=True)
      try:
        lentoshow = int(command[1])
      except:
        lentoshow = lb_default
      if int(lentoshow)>len(data):
        lentoshow=len(data)
      data = data[:lentoshow]
      
      embed = discord.Embed(title="Leaderboard",color=discord.Color.blue())
      i=1
      for info in data:
        embed.add_field(name=str(i)+". "+str(info["Name"]),value=":coin: BC "+str(info["Balance"]),inline=False)
        i+=1
      await message.channel.send(embed=embed)
  except Exception as error:
    #if error send error message
    await message.channel.send(errorOccured+str(error))


async def update(message, command, op):
  if op: #so only op can use this command
    # for Testing
    #await message.channel.send("Update!!")

    try:
      if updateData():
        await message.channel.send(updateSuccess)
      else:
        await message.channel.send(unknownError)
    except Exception as error:
      await message.channel.send(errorOccured+str(error))
  else:
    await message.channel.send("You dont have permission to use that")
