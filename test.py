import discord
from settings import t_cmds,empty_space,empty_spaces
from tools import getAccountsData,getReminderData

async def tExecuteCommand(message,command, op):
  for cmd in t_cmds["showdata"]:
    if command[0] == cmd:
        await showdata(message,op)
  for cmd in t_cmds["showreminder"]:
    if command[0] == cmd:
        await showreminder(message,op)


async def showdata(message,op):
  data_list = getAccountsData()

  desc="Data list"+empty_spaces+"\n"+empty_space
  embed = discord.Embed(title="Accounts Data",description=desc)
  i=1
  for info in data_list:
    keys = info.keys()
    temp=""
    for key in keys:
      temp= "{}{}:{}".format(temp,key,info[key])+empty_spaces
    
    embed.add_field(name=str(i),
    value=temp+"\n"+ empty_space ,inline=False)
    if i%5 == 0:
      await message.channel.send(embed=embed)
      embed = discord.Embed(title="Accounts Data",description=desc)
    i+=1
  await message.channel.send(embed=embed)
  


async def showreminder(message,op):
  data_list = getReminderData()

  desc="Data list"+empty_spaces+"\n"+empty_space
  embed = discord.Embed(title="Reminder Data",description=desc)
  i=1
  for info in data_list:
    keys = info.keys()
    temp=""
    for key in keys:
      temp= "{}{}:{}".format(temp,key,info[key])+empty_spaces
    embed.add_field(name=str(i),
    value=temp+"\n"+ empty_space ,inline=False)
    i+=1

  await message.channel.send(embed=embed)