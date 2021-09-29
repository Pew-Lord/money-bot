import discord
from discord.ext import commands
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
    await message.channel.send("(1/{}) {}".format(msgnum, msg1))
    await message.channel.send("(2/{}) {}".format(msgnum, msg2))
    await message.channel.send("(3/{}) {}".format(msgnum, msg3))
    await message.channel.send("(4/{}) {}".format(msgnum, msg4))
    if msg5 != "":
        await message.channel.send("(5/5) {}".format(msg5))

@bot.command()
async def allprices(message, arg = ""):
    await message.channel.send("All item Prices: ".format(bz.itemprices()))

@bot.command()
async def allvalues(message, arg = ""):
    await message.channel.send("All Item Values: ".format(bz.itemvalues()))

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