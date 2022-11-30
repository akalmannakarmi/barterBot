import discord
from settings import bb_cmds,accDoesNotExist,errorOccured,bank_rates_title,bank_rates_desc,uDontHaveAcc,couldNotAddMoney,improperData_msg,time_format,one_day,one_hour,one_min,one_week,one_month,bank_rates,disabled_msg
from tools import getAccountInfo,canClaimInvested,claimInvested_,InvestedclaimTimeleft,canWithdrawSavings,canAddSavings,addSavings_,invest_,canInvest,withdrawSavings_

async def bExecuteCommand(message,command, op):
  for cmd in bb_cmds["savings"]:
    if command[0] == cmd:
        await showSavings(message, command, op)
  for cmd in bb_cmds["invested"]:
    if command[0] == cmd:
        await showInvested(message, command, op)
  for cmd in bb_cmds["claim"]:
    if command[0] == cmd:
        await claimInvested(message, command, op)
  for cmd in bb_cmds["withdraw"]:
    if command[0] == cmd:
        await withdrawSavings(message, command, op)
  for cmd in bb_cmds["addsavings"]:
    if command[0] == cmd:
        await message.channel.Send(disabled_msg)
        #await addSavings(message, command, op)
  for cmd in bb_cmds["invest"]:
    if command[0] == cmd:
        await message.channel.Send(disabled_msg)
        #await invest(message, command, op)
  for cmd in bb_cmds["rates"]:
    if command[0] == cmd:
        await showRates(message, command, op)


async def showSavings(message,command,op):
  #await message.channel.send("Show Savings!!")    #for testing

  #Id of user
  try:
    idC = message.mentions[0].id  #if they mentions some one use that id
  except:
    idC = message.author.id

  try:
    info = getAccountInfo(idC) #Get info of user to claim

    if info == False:  #if did not find the account of the user
      await message.channel.send(accDoesNotExist) #Error message
      return
    else:
      embed = discord.Embed(title="Savings",color=discord.Color.blue())
      embed.add_field(name=str(info["Name"]),value=":coin: BC "+str(info["Banked"]),inline=False)
      await message.channel.send(embed=embed) #The Savings info
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def showInvested(message,command,op):
  #await message.channel.send("Show Invested!!")    #for testing

  #Id of user
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
      embed = discord.Embed(title="Invested",color=discord.Color.blue())
      embed.add_field(name=str(info["Name"]),value=":coin: BC "+str(info["Invested"]),inline=False)
      await message.channel.send(embed=embed) #Send Invested Info
  except Exception as error:
    await message.channel.send(errorOccured+str(error)) 


async def claimInvested(message,command,op):
  #await message.channel.send("claim Invested") #For testing

  try:
    #get ID
    if op: #so op can claim for others
      try:
        idC = message.mentions[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id

    info = getAccountInfo(idC) #Get info of user

    if info == False:  #if did not find the account of the user
      await message.channel.send(uDontHaveAcc) #error
      return
    else:
      if canClaimInvested(idC):
        if claimInvested_(idC):
          await message.channel.send(f"Successfully claimed Invested!!")
        else:
          await message.channel.send(couldNotAddMoney)
      else:
        timeLeft = InvestedclaimTimeleft(idC)
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


async def withdrawSavings(message,command,op):
  #await message.channel.send("withdraw Savings") #For testing

  try:
    #Get ID
    if op: #so op can withdaw for others
      try:
        idC = message.mentions[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id

    try:
      amount = float(command[1])  #amount to withdaw
      if amount <= 0:
        await message.channel.send(improperData_msg) #cant withdaw negative
        return
    except:
      await message.channel.send(improperData_msg) #error
      return

    info = getAccountInfo(idC) #Get info of user

    if info == False:  #if did not find the account of the user
      await message.channel.send(uDontHaveAcc)
      return
    else:
      if canWithdrawSavings(idC,amount):
        if withdrawSavings_(idC,amount):
          await message.channel.send(f"Successfully withdrawn :coin: BC {amount}")
        else:
          await message.channel.send(couldNotAddMoney)
      else:
        await message.channel.send(f"Sorry you can not withdraw :coin: BC {amount}")
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def addSavings(message,command,op):
  #await message.channel.send("add Savings") #For testing

  try:
    #get ID
    if op: #so op can add savings for others
      try:
        idC = message.mentions[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id

    try:
      amount = float(command[1]) #amount to add
    except:
      await message.channel.send(improperData_msg)
      return
    
    info = getAccountInfo(idC) #Get info of user

    if info == False:  #if did not find the account of the user
      await message.channel.send(uDontHaveAcc) #error
      return
    else:
      if canAddSavings(idC,amount):
        if addSavings_(idC,amount):
          await message.channel.send(f"Successfully added :coin: BC {amount} to savings")
        else:
          await message.channel.send(couldNotAddMoney)
      else:
        await message.channel.send(f"Sorry you can not add :coin: BC {amount} to savings")
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def invest(message,command,op):
  #await message.channel.send("invest") #For testing

  try:
    #get ID
    if op: #so op can invest for others
      try:
        idC = message.mentions[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id
      
    info = getAccountInfo(idC) #Get info of user to claim
    try:
      #To get the Time to invest for
      amount = float(command[1])
      timeTo_ = float(command[2])
      timeUnit = str(command[3])
      for times in time_format['seconds']:
        if timeUnit == times:
          temp = timeTo_ * 1
      for times in time_format['minutes']:
        if timeUnit == times:
          temp = timeTo_ * one_min
      for times in time_format['hours']:
        if timeUnit == times:
          temp = timeTo_ * one_hour
      for times in time_format['days']:
        if timeUnit == times:
          temp = timeTo_ * one_day
      for times in time_format['weeks']:
        if timeUnit == times:
          temp = timeTo_ * one_week
      for times in time_format['months']:
        if timeUnit == times:
          temp = timeTo_ * one_month
      timeTo = temp
    except:
      await message.channel.send(improperData_msg) #error
      return

    if info == False:  #if did not find the account of the user
      await message.channel.send(uDontHaveAcc)
      return
    else:
      if canInvest(idC,amount):
        if invest_(idC,amount,timeTo):
          await message.channel.send(f"Successfully invested :coin: BC {amount} for {timeTo_} {timeUnit}")
        else:
          await message.channel.send(couldNotAddMoney)
      else:
        await message.channel.send(f"Sorry you can not invest :coin: BC {amount}")
  except Exception as error:
    await message.channel.send(errorOccured+str(error))


async def showRates(message,command,op):
  #await message.channel.send("Show Rates") # Fortesting
  
  embed = discord.Embed(title=bank_rates_title,description=bank_rates_desc,color=discord.Color.red())
  for field in bank_rates:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed) #Send the rates
