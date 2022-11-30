import discord
from settings import help_cmds,bch_title,bch_desc,bch,bbh,bbh_desc,bbh_title,calch_title,calch_desc,calch,gh,gh_title,gh_desc,hm,hm_title,hm_desc,bchd_title,bchd_desc,bchd,bbhd,bbhd_desc,bbhd_title,calchd_title,calchd_desc,calchd,ghd,ghd_title,ghd_desc,dhm,dhm_title,dhm_desc,mch,mch_title,mch_desc,mchd,mchd_title,mchd_desc

async def botHelpBartercoin(message):

  embed = discord.Embed(title=bch_title,description=bch_desc,color=discord.Color.red())
  for field in bch:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)


async def botHelpBarterbank(message):

  embed = discord.Embed(title=bbh_title,description=bbh_desc,color=discord.Color.red())
  for field in bbh:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)


async def botHelpCalculator(message):
  embed = discord.Embed(title=calch_title,description=calch_desc,color=discord.Color.red())
  for field in calch:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)
  

async def botHelpGeneral(message):

  embed = discord.Embed(title=gh_title,description=gh_desc,color=discord.Color.red())
  for field in gh:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)


async def botHelpMinecraft(message):

  embed = discord.Embed(title=mch_title,description=mch_desc,color=discord.Color.red())
  for field in mch:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)


async def botHelpMenu(message):
  
  embed = discord.Embed(title=hm_title,description=hm_desc,color=discord.Color.red())
  for field in hm:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=True)

  await message.channel.send(embed=embed)


async def botHelp(message,command,op):
  command_found=False
  try:
    for cmd in help_cmds["bartercoin"]:
      if command[1] == cmd:
          command_found=True
          await botHelpBartercoin(message)
    for cmd in help_cmds["barterbank"]:
      if command[1] == cmd:
          command_found=True
          await botHelpBarterbank(message)
    for cmd in help_cmds["general"]:
      if command[1] == cmd:
          command_found=True
          await botHelpGeneral(message)
    for cmd in help_cmds["calculator"]:
      if command[1] == cmd:
          command_found=True
          await botHelpCalculator(message)
    for cmd in help_cmds["minecraft"]:
      if command[1] == cmd:
          command_found=True
          await botHelpMinecraft(message)
  except:
    pass
  if not command_found:
    await botHelpMenu(message)


async def botHelpdetailBartercoin(message):

  embed = discord.Embed(title=bchd_title,description=bchd_desc,color=discord.Color.red())
  for field in bchd:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)
  
  await message.channel.send(embed=embed)


async def botHelpdetailBarterbank(message):
  
  embed = discord.Embed(title=bbhd_title,description=bbhd_desc,color=discord.Color.red())
  for field in bbhd:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)

  await message.channel.send(embed=embed)


async def botHelpdetailCalculator(message):
  
  embed = discord.Embed(title=calchd_title,description=calchd_desc,color=discord.Color.red())
  for field in calchd:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)

  await message.channel.send(embed=embed)
  

async def botHelpdetailGeneral(message):
 
  embed = discord.Embed(title=ghd_title,description=ghd_desc,color=discord.Color.red())
  for field in ghd:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)

  await message.channel.send(embed=embed)


async def botHelpdetailMinecraft(message):
 
  embed = discord.Embed(title=mchd_title,description=mchd_desc,color=discord.Color.red())
  for field in mchd:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)

  await message.channel.send(embed=embed)


async def botHelpdetailMenu(message):
  
  embed = discord.Embed(title=dhm_title,description=dhm_desc,color=discord.Color.red())
  for field in dhm:
    embed.add_field(name=field["name"],
    value=field["value"] ,inline=False)

  await message.channel.send(embed=embed)


async def botHelpdetail(message,command,op):
  command_found=False
  try:
    for cmd in help_cmds["bartercoin"]:
      if command[1] == cmd:
          command_found=True
          await botHelpdetailBartercoin(message)
    for cmd in help_cmds["barterbank"]:
      if command[1] == cmd:
          command_found=True
          await botHelpdetailBarterbank(message)
    for cmd in help_cmds["general"]:
      if command[1] == cmd:
          command_found=True
          await botHelpdetailGeneral(message)
    for cmd in help_cmds["calculator"]:
      if command[1] == cmd:
          command_found=True
          await botHelpdetailCalculator(message)
    for cmd in help_cmds["minecraft"]:
      if command[1] == cmd:
          command_found=True
          await botHelpdetailMinecraft(message)
  except:
    pass
  if not command_found:
    await botHelpdetailMenu(message)