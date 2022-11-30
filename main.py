import Keep_Alive
import discord
import os
from replit import db
import asyncio

from tools import isOP,separate_cmds,getOperatorIndex,calculate,reminderThread,bankThread,dailyReminderThread
from settings import calculate_prefixs,bank_prefixs,coin_prefixs,test_prefixs,general_prefixs,minecraft_prefixs,operators,bot_prefix,hiddenFound_msg,easterEggs
from coin import bcExecuteCommand
from bank import bExecuteCommand
from general import gExecuteCommand
from test import tExecuteCommand
from minecraft import mcExecuteCommand

#When db is cleared
#db.set("data",[])
#db.set("reminderList",[])
#db.set("lastDayChange",float(1627755348))
try:
  data = db.get("data")
except:
  print("failed")


client = discord.Client()


@client.event
async def on_ready():
  #print(data)
  await client.change_presence(status=discord.Status.idle,activity=discord.Game("b!help"))
  print('We have logged in as {0.user}'.format(client))
  asyncio.get_event_loop().create_task(reminderThread(client))
  asyncio.get_event_loop().create_task(bankThread())
  asyncio.get_event_loop().create_task(dailyReminderThread(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith(bot_prefix):
    #testing
    #await message.channel.send(response)

    #separating message from prefix
    text = message.content
    mp_text = text[len(bot_prefix):] #Removes the Prefix

    if mp_text[0] == " ":           #Some times there is no space so if there is remove
      mp_text = mp_text.strip(" ")
    
    #separating messages with spaces
    commands=separate_cmds(mp_text)
    print(commands,message.author.name) #Testing thing prints our the commands separated

    try:
      prefix2 = commands[0]
    except:
      await generalPart(None,commands,message)
    if prefix2 != None:
      for cmd in easterEggs.keys():
        if prefix2 == cmd:
          await message.channel.send(easterEggs[prefix2])
      for cmd in coin_prefixs:
        if prefix2 == cmd:
          await coinPart(cmd,commands,message)
          return
      for cmd in bank_prefixs:
        if prefix2 == cmd:
          await bankPart(cmd,commands,message)
          return
      for cmd in calculate_prefixs:
        if prefix2 == cmd:
          await calculatorPart(cmd,commands,message)
          return
      for cmd in general_prefixs:
        if prefix2 == cmd:
          await generalPart(cmd,commands,message)
          return
      for cmd in minecraft_prefixs:
        if prefix2 == cmd:
          await minecraftPart(cmd,commands,message)
          return
      for cmd in test_prefixs:
        if prefix2 == cmd:
          await testPart(cmd,commands,message)
          return
      #await botHelpMenu(message)
      await generalPart(None,commands,message)
    
async def coinPart(prefix,commands,message):
  #testing
  #await message.channel.send(response)
  commands.remove(prefix)
  # OP condition
  op = isOP(message)

  #execute commands
  await bcExecuteCommand(message,commands,op)


async def bankPart(prefix,commands,message):
  #testing
  #await message.channel.send("banke")

  #separating message from prefix
  commands.remove(prefix)

  # OP condition
  op = isOP(message)

  #execute commands
  await bExecuteCommand(message,commands,op)


async def generalPart(prefix,commands,message):
  #testing
  #await message.channel.send("General")

  #separating message from prefix
  if prefix != None:
    commands.remove(prefix)

  # OP condition
  op = isOP(message)

  #execute commands
  await gExecuteCommand(message,commands,op,client)


async def minecraftPart(prefix,commands,message):
  #testing
  #await message.channel.send("Minecraft")

  #separating message from prefix
  if prefix != None:
    commands.remove(prefix)

  # OP condition
  op = isOP(message)

  #execute commands
  await mcExecuteCommand(message,commands,op,client)


async def calculatorPart(prefix,commands,message):
  #testing
  #await message.channel.send(response)

  #separating message from prefix
  commands.remove(prefix)

  #unseparating the commands
  mp_text=""
  for cmd in commands:
    mp_text += cmd
  
  #separate the inputs
  operator_index,operator = getOperatorIndex(operators,mp_text)
  first_num = float(mp_text[:operator_index])
  second_num = float(mp_text[operator_index+1:])

  #calculate
  result = calculate(first_num,second_num,operator)
  await message.channel.send("result="+str(result))


async def testPart(prefix,commands,message):
  #testing
  #await message.channel.send("General")

  #separating message from prefix
  commands.remove(prefix)
  
  # OP condition
  op = isOP(message)

  if op:
    await tExecuteCommand(message,commands,op)
  else:
    await message.channel.send(hiddenFound_msg)


Keep_Alive.keep_alive()
client.run(os.environ['TOKEN'])