# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import discord # i did not make this module
from discord.ext import commands # i did not make this module
import bzpricesfunctions as bz

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def Items(message, arg = ""):
    msg1, msg2, msg3, msg4, msg5 = bz.itemnames()
    if msg5 != "":
        msgnum = 5
    else:
        msgnum = 4
    await message.channel.send("(1/{})```{}```".format(msgnum, msg1))
    await message.channel.send("(2/{})```{}```".format(msgnum, msg2))
    await message.channel.send("(3/{})```{}```".format(msgnum, msg3))
    await message.channel.send("(4/{})```{}```".format(msgnum, msg4))
    if msg5 != "":
        await message.channel.send("(5/5)```{}```".format(msg5))

@bot.command()
async def allprices(message, arg = ""):
    msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9 = bz.itemprices()
    if msg9 == "":
        msgnum = 8
    else:
        msgnum = 9
    await message.channel.send("Please note, if an item's price is equal to -1, then it has no active sell orders.")
    await message.channel.send("(1/{})```{}```".format(msgnum, msg1))
    await message.channel.send("(2/{})```{}```".format(msgnum, msg2))
    await message.channel.send("(3/{})```{}```".format(msgnum, msg3))
    await message.channel.send("(4/{})```{}```".format(msgnum, msg4))
    await message.channel.send("(5/{})```{}```".format(msgnum, msg5))
    await message.channel.send("(6/{})```{}```".format(msgnum, msg6))
    await message.channel.send("(7/{})```{}```".format(msgnum, msg7))
    await message.channel.send("(8/{})```{}```".format(msgnum, msg8))      
    if msgnum == 9:
        await message.channel.send("(9/9)```{}```".format(msg9))

@bot.command()
async def allvalues(message, arg = ""):
    msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9 = bz.itemvalues()
    if msg9 == "":
        msgnum = 8
    else:
        msgnum = 9
    await message.channel.send("Please note, if an item's price is equal to -1, then it has no active sell orders.")
    await message.channel.send("(1/{})```{}```".format(msgnum, msg1))
    await message.channel.send("(2/{})```{}```".format(msgnum, msg2))
    await message.channel.send("(3/{})```{}```".format(msgnum, msg3))
    await message.channel.send("(4/{})```{}```".format(msgnum, msg4))
    await message.channel.send("(5/{})```{}```".format(msgnum, msg5))
    await message.channel.send("(6/{})```{}```".format(msgnum, msg6))
    await message.channel.send("(7/{})```{}```".format(msgnum, msg7))
    await message.channel.send("(8/{})```{}```".format(msgnum, msg8))      
    if msgnum == 9:
        await message.channel.send("(9/9)```{}```".format(msg9))

@bot.command()
async def Price(message, arg):
    await message.channel.send("{} costs {} coins each.".format(message, bz.specificitemprice(message)))

@bot.command()
async def value(message, arg):
    await message.channel.send("{} is worth {} coins each.".format(message, bz.specificitemvalue(message)))
'''
message.author.mention (@'s the author)
message.channel.send (sends message in channel)
'''
keyfile = open("botkey.txt", "r")
botkey = keyfile.readlines()
bot.run(botkey[0])