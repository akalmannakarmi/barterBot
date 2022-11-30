import discord
from settings import mc_cmds,taskChannelid,noChannel_msg,improperData_msg,wl_noServerSent_msg,wl_requestSent_msg,ip

client = discord.Client()

async def mcExecuteCommand(message,command, op,client):
  for cmd in mc_cmds["whitelist"]:
    if command[0] == cmd:
      await whitelistMe(message,command,op,client)
  for cmd in mc_cmds["ip"]:
    if command[0] == cmd:
      await showIP(message)

async def showIP(message):
  await message.channel.send(ip) #Sends he Ip


async def whitelistMe(message,command,op,client):
  noerror = True
  #await message.channel.send("whitelistMe")

  #idC = message.author.id
  nameC = message.author.name    #Get info of who messaged
  #discriminator = message.author.discriminator

  try:
    username=command[1]   #Get the IGN aka minecraft username
  except:
    noerror = False
  try:
    server = command[2]  #Get which server to whitelist
  except:
    server = wl_noServerSent_msg
  if noerror:
    toSend=f"""Whitelist request
By:{nameC}
Server:{server}
Username:{username}
"""
    taskchannel = client.get_channel(taskChannelid)  #Get the channel to send task to
    if taskchannel == None:
      await message.channel.send(noChannel_msg) #No Channel Error message
    else:
      await taskchannel.send(toSend) #Send Task
      await message.channel.send(wl_requestSent_msg) #Success message
  else:
    await message.channel.send(improperData_msg) #Error message