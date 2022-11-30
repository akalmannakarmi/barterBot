import discord
import time
import random
from replit import db
from settings import g_cmds,taskChannelid,noChannel_msg,improperData_msg,wl_noServerSent_msg,wl_requestSent_msg,ip,time_format,one_min,one_day,one_hour,couldNotGetDB,errorOccured,reminderSet,reminderRemoved,unknownError
from help_ import botHelp,botHelpdetail
from tools import removeReminderInfo

client = discord.Client()

async def gExecuteCommand(message,command, op,client):
  for cmd in g_cmds["helpdetail"]:
    if command[0] == cmd:
        await botHelpdetail(message, command, op)
  for cmd in g_cmds["help"]:
    if command[0] == cmd:
        await botHelp(message, command, op)
  for cmd in g_cmds["remindme"]:
    if command[0] == cmd:
      await remindMe(message,op,command)
  for cmd in g_cmds["removereminder"]:
    if command[0] == cmd:
      await removeReminder(message,op,command)
  for cmd in g_cmds["flipacoin"]:
    if command[0] == cmd:
      await flipACoin(message)


async def flipACoin(message):
  #await message.channel.send("remindme") #for testing
  output = random.randrange(1,3)
  if output == 1:
    await message.channel.send("Heads")
  elif output == 2:
    await message.channel.send("Tails")
  else:
    print(output)
    await message.channel.send(unknownError)

async def removeReminder(message,op,command):
   #await message.channel.send("remindme") #for testing
  try:
    if op:
      try:
        idC = message.mention[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id  #get id to remind

    try:
      removeReminderInfo(idC)
      await message.channel.send(reminderRemoved)
    except:
      await message.channel.send(couldNotGetDB)
  except Exception as error:
    await message.channel.send(errorOccured+str(error))



async def remindMe(message,op,command):
  #await message.channel.send("remindme") #for testing
  try:
    if op:
      try:
        idC = message.mention[0].id
      except:
        idC = message.author.id
    else:
      idC = message.author.id  #get id to remind
    
    try:
      remindTimeNo = float(command[1])
      remindTimeIn = str(command[2])
      command.pop(0)
      command.pop(0)
      command.pop(0)
      remindReason = ""
      for cmd in command:
        remindReason = f"{remindReason} {cmd}"
    except:
      await message.channel.send(improperData_msg)
      return

    for times in time_format['seconds']:
      if remindTimeIn == times:
        remindTime = remindTimeNo * 1
    for times in time_format['minutes']:
      if remindTimeIn == times:
        remindTime = remindTimeNo * one_min
    for times in time_format['hours']:
      if remindTimeIn == times:
        remindTime = remindTimeNo * one_hour
    for times in time_format['days']:
      if remindTimeIn == times:
        remindTime = remindTimeNo * one_day
    remindTimeExact = remindTime+time.time()
    reminder = {"ID":idC,
                "Time":remindTimeExact,
                "Reason":remindReason,
                "Repeat":str(False),
                "Interval":remindTime}

    try:
      reminderList = db.get("reminderList")
      reminderList.append(reminder)
      db.set("reminderList",reminderList)
      await message.channel.send(reminderSet)
    except:
      await message.channel.send(couldNotGetDB)
  except Exception as error:
    await message.channel.send(errorOccured+str(error))
