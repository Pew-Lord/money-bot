# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import discord # i did not make this module
from discord.ext import commands # i did not make this module
import bzpricesfunctions as bz
from time import sleep
import auctionprices as ah
bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is running, time to make money!")

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
    sleep(3)
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
    sleep(3)
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
async def price(message, arg, arg2 = "", arg3 = "", arg4 = "", arg5 = ""):
    args = []
    lastarg = 1
    if arg2 == "":
        lastarg = 2
        args.append(arg)
    elif arg3 == "":
        lastarg = 3
        args.append(arg)
        args.append(arg2)
    elif arg4 == "":
        lastarg = 4
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
    elif arg5 == "":
        lastarg = 5
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
        args.append(arg4)
    elif arg5 != "":
        lastarg = 6
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
        args.append(arg4)
        args.append(arg5)
    else:
        args.append(arg)
    newarg = " ".join(args)
    if bz.specificitemprice(newarg) == -1:
        await message.channel.send("```There are currently no sell orders for {}```".format(newarg))
    else:
        await message.channel.send("```{} is worth {} coins each.```".format(newarg, bz.specificitemprice(newarg)))

@bot.command()
async def value(message, arg, arg2 = "", arg3 = "", arg4 = "", arg5 = ""):
    args = []
    lastarg = 1
    if arg2 == "":
        lastarg = 2
        args.append(arg)
    elif arg3 == "":
        lastarg = 3
        args.append(arg)
        args.append(arg2)
    elif arg4 == "":
        lastarg = 4
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
    elif arg5 == "":
        lastarg = 5
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
        args.append(arg4)
    elif arg5 != "":
        lastarg = 6
        args.append(arg)
        args.append(arg2)
        args.append(arg3)
        args.append(arg4)
        args.append(arg5)
    else:
        args.append(arg)
    newarg = " ".join(args)
    if bz.specificitemvalue(newarg) == -1:
        await message.channel.send("```There are currently no buy orders for {}```".format(newarg))
    else:
        await message.channel.send("```{} is worth {} coins each.```".format(newarg, bz.specificitemvalue(newarg)))
@bot.command()
async def ahprice(message, *args):
    arg = " ".join(args)
    await message.channel.send("This may take some time...")
    msg = ah.getitemprice(arg)
    if msg[0] == "N/A" or msg[1] == -1 or msg[2] == "N/A":
        await message.channel.send("Sorry, but there are no bin auctions for {}.".format(arg))
    else:
        msgstr = "The cheapest {} is {}, you can look at the auction with the command /viewauction {}".format(msg[0], msg[1], msg[2])
        await message.channel.send("{}, {}".format(message.author.mention, msgstr))
@bot.command()
async def star(message):
    await message.channel.send("✪")

'''
message.author.mention (@'s the author)
message.channel.send (sends message in channel)
'''

keyfile = open("./Python/money-bot/botkey.txt", "r")
botkey = keyfile.readlines()
bot.run(botkey[0])