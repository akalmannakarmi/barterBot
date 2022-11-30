from replit import db
from settings import db_format,one_day,loginreward,loginStreakBonus,reminderRunning,bankRunning,bank_saveings_rate,bank_invest_rate,bank_min_saveings,dailyReminder_msg,bank_min_invest,coinRunning,op_id
import math
import time
import ast
import asyncio

def getTime(epochTime):
  years = math.floor(epochTime/3.154e+7)
  temp = epochTime%3.154e+7
  months = math.floor(temp/2.628e+6)
  temp = temp%2.628e+6
  days = math.floor(temp/86400)
  temp = temp%86400
  hours = math.floor(temp/3600)
  temp = temp%3600
  minutes = math.floor(temp/60)
  temp = temp%60
  seconds = math.floor(temp)

  splitedTime={"years":years,
               "months":months,
               "days":days,
               "hours":hours,
               "minutes":minutes,
               "seconds":seconds}
  return splitedTime

def getBal(info):
  return float(info["Balance"])


def getOperatorIndex(operators, text):
    for operator in operators:
        operator_index = text.find(operator)
        if operator_index != -1:
            return operator_index, operator


def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    if operator == "%":
        return num1 % num2
    if operator == "^":
        return pow(num1, num2)


def separate_cmds(text):
    cmds = []
    word = ""
    for letter in text:
        if letter == " ":
            cmds.append(word)
            word = ""
        else:
            word += letter
    cmds.append(word)
    return cmds


def isOP(message):
  for idC in op_id:
      if str(idC) == str(message.author.id):
          return True
  return False


def getList(data):
  temp = ast.literal_eval(data)
  return temp


def can_invest(idC,amount):
    data = getAccountsData()
    for info in data:
      if str(info["ID"]) == str(idC):
        if float(info["Balance"]) >= float(amount):
          return True
        else:
          return False
    return False


def checkHasAccount(idC):
  data = getAccountsData()
  for info in data:
    if str(info["ID"]) == str(idC):
      return True
  return False


def getAccountsData():
  data = db.get_raw("data")
  return ast.literal_eval(data)


def getReminderData():
  data = db.get_raw("reminderList")
  return ast.literal_eval(data)


def getReminderInfo(idC):
  data = getReminderData()
  for info in data:
    if str(info["ID"])==str(idC):
      return info
  return False


def removeReminderInfo(idC):
  reminderList = getReminderData()
  for info in reminderList:
    if str(info["ID"]) == str(idC):
      reminderList.remove(info)
      db.set("reminderList",reminderList)
      removeReminderInfo(idC)
      return
  db.set("reminderList",reminderList)


def getAccountInfo(idC):
  data = getAccountsData()
  for info in data:
    if str(info["ID"])==str(idC):
      return info
  return False


def canClaimDaily(idC):
  info = getAccountInfo(idC)
  if info != False:
    if time.time()-info["Lastclaimed"] >= one_day:
      return True
  return False


def dailyReward(idC):
  info = getAccountInfo(idC)
  if info != False:
    reward = round(loginreward*(1+info['Loginstreak']*loginStreakBonus),2)
    return reward
  return 0


def DailyclaimTimeleft(idC):
  info = getAccountInfo(idC)
  if info != False:
    lastClaimed = info["Lastclaimed"]
    timeleft_sec = one_day - (time.time()-lastClaimed) 
    timeleft = getTime(timeleft_sec)
    return timeleft


def claimDaily_(idC,amount):
  data = getAccountsData()
  for info in data:
    if str(info["ID"]) == str(idC):
      info["Balance"] = round((float(info["Balance"])+float(amount)),2)
      info["Lastclaimed"] = time.time()
      info["Loginstreak"] = int(info["Loginstreak"]) + 1
      if setData(data):
        return True
      else:
        return False


def addMoney(idC,amount):
  data = getAccountsData()
  for info in data:
    if str(info["ID"]) == str(idC):
      info["Balance"] = float(info["Balance"])+float(amount)
      if setData(data):
        return True
      else:
        return False


def setMoney(idC,amount):
  data = getAccountsData()
  for info in data:
    if str(info["ID"]) == str(idC):
      info["Balance"] = float(amount)
      if setData(data):
        return True
      else:
        return False


def setData(data):
  try:
    db.set("data",data)
    return True
  except:
    print("Could Not Set data")
    return False


def delAccount(idC):
  data = getAccountsData()
  info = getAccountInfo(idC)
  data.remove(info)
  if setData(data):
    return True
  else:
    return False


def transferMoney(fromID,toID,amount):
  data = getAccountsData()
  fromInfo = getAccountInfo(fromID)
  toInfo = getAccountInfo(toID)
  fromIndex = data.index(fromInfo)
  toIndex = data.index(toInfo)

  if float(fromInfo["Balance"]) >= float(amount):
    data[fromIndex]["Balance"] = float(data[fromIndex]["Balance"]) - amount 
    data[toIndex]["Balance"] = float(data[toIndex]["Balance"]) + amount
    if setData(data):
      return True
  return False


def updateData():
  data = getAccountsData()
  for info in data:
    for key in db_format:
      try:
        temp = info[key]
      except:
        info[key] = 0
  if setData(data):
    return True
  else:
    return False


async def reminderThread(client):
  while reminderRunning:
    reminderList = ast.literal_eval(db.get_raw("reminderList"))
    for info in reminderList:
      if float(info["Time"]) <= float(time.time()):
        target = await client.fetch_user(info["ID"])
        await target.send("Reminder"+ " "+info["Reason"])
        if str(info["Repeat"])== "True":
          info["Time"] = float(info["Time"])+float(info["Interval"])
        else:
          reminderList.remove(info)
        db.set("reminderList",reminderList)
    await asyncio.sleep(1)


async def bankThread():
  while bankRunning:
    lastDayChange = db.get("lastDayChange")
    if float(time.time()) >= float(lastDayChange)+float(one_day):
      db.set("lastDayChange",float(time.time()))
      data = getAccountsData()
      for info in data:
        info["Banked"] = round((float(info["Banked"]) * (1+bank_saveings_rate)),2)
        info["Invested"] = round((float(info["Invested"]) * (1+bank_invest_rate)),2)
      setData(data)
    await asyncio.sleep(1)

  
async def dailyReminderThread(client):
  while coinRunning:
    try:
      data = getAccountsData()
      for info in data:
        if int(info["Dailyreminder"]) == 1:
          if float(info["Lastclaimed"])+one_day <= float(time.time()):
            target = await client.fetch_user(info["ID"])
            await target.send(dailyReminder_msg)
            info["Dailyreminder"] = 2
        elif int(info["Dailyreminder"]) == 2:
          if float(info["Lastclaimed"])+one_day >= float(time.time()):
            info["Dailyreminder"] = 1
    except Exception as error:
      print("error here at tools dailyReminderThread"+str(error))
    setData(data)
    await asyncio.sleep(1)


def canClaimInvested(idC):
  info = getAccountInfo(idC)
  if info == False:
    return False
  else:
    if float(time.time())-float(info["Investend"]) >= 0:
      return True
  return False


def claimInvested_(idC):
  data = getAccountsData()
  for info in data:
    if str(info["ID"]) == str(idC):
      info["Balance"] = float(info["Balance"])+float(info["Invested"])
      info["Invested"] = 0
      if setData(data):
        return True
      else:
        return False
  return False


def InvestedclaimTimeleft(idC):
  info = getAccountInfo(idC)
  timeLeft_ = float(info["Investend"]) - float(time.time())
  timeLeft = getTime(timeLeft_)
  return timeLeft


def canWithdrawSavings(idC,amount):
  info = getAccountInfo(idC)
  if info != False:
    if float(info["Banked"]) >= float(amount):
      return True
  return False


def withdrawSavings_(idC,amount):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Balance"] = float(info["Balance"])+float(amount)
        info["Banked"] = float(info["Banked"])-float(amount)
        setData(data)
        return True
  return False


def canAddSavings(idC,amount):
  info = getAccountInfo(idC)
  if info != False:
    if float(info["Balance"]) >= float(amount) and float(amount) >= bank_min_saveings:
      return True
  return False


def addSavings_(idC,amount):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Banked"] = float(info["Banked"])+float(amount)
        info["Balance"] = float(info["Balance"])-float(amount)
        setData(data)
        return True
  return False


def canInvest(idC,amount):
  info = getAccountInfo(idC)
  if info != False:
    if float(info["Balance"]) >= float(amount) and float(amount) >= bank_min_invest and float(info["Invested"]) == 0:
      return True
  return False


def invest_(idC,amount,timeTo):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Invested"] = float(amount)
        info["Balance"] = float(info["Balance"])-float(amount)
        info["Investend"] = float(time.time())+float(timeTo)
        setData(data)
        return True
  return False

    
def enableDailyReminder(idC):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Dailyreminder"] = 1
        setData(data)
        return True
  return False


def disableDailyReminder(idC):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Dailyreminder"] = 0
        setData(data)
        return True
  return False


def sentDailyReminder(idC):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Dailyreminder"] = 2
        setData(data)
        return True
  return False


def updateName_(idC,nameC,discriminatorC):
  data = getAccountsData()
  if data != False:
    for info in data:
      if str(info["ID"]) == str(idC):
        info["Name"] = nameC
        info["Discriminator"] = discriminatorC
        if setData(data):
          return True
  return False
        
