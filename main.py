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
# help - "commands: $items - sends all items in the hypixel skyblock bazaar. $allprices - sends all items in the hypixel skyblock bazaar along with their price. $allvalues - sends all items in the hypixel skyblock bazaar along with their value.$price item - sends the price of a specific item (item is replaced with the name of the item you want) $value item - sends the value of a specific item (item is replaced with the name of the item you want) $ahprice item - sends the lowest price for a specific item on the auction house (item is replaced with the name of the item you want) $gt amount - sends the amount of wolf teeth & enchanted gold to buy to craft a certain amount of golden teeth, and how much profit you will recieve.$star - sends the star used in item names, the star can be used to find the item price of the item with a certain number of stars."
@bot.command()
async def Items(message, arg = ""):
    msg1, msg2, msg3, msg4, msg5 = bz.newItems()
    if msg5 != "":
        msgnum = 5
    else:
        msgnum = 4
    print(message.author)
    await message.channel.send("(1/{})```{}```".format(msgnum, msg1))
    await message.channel.send("(2/{})```{}```".format(msgnum, msg2))
    await message.channel.send("(3/{})```{}```".format(msgnum, msg3))
    await message.channel.send("(4/{})```{}```".format(msgnum, msg4))
    if msg5 != "":
        await message.channel.send("(5/5)```{}```".format(msg5))

@bot.command()
async def allprices(message, arg = ""):
    msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9 = bz.newPrices()
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
    msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9 = bz.newValues()
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
async def price(message, *args):
    newarg = " ".join(args)
    try:
        if bz.specificitemprice(newarg) == -1:
            await message.channel.send("```There are currently no sell orders for {}```".format(newarg))
        else:
            await message.channel.send("```{} is worth {} coins each.```".format(newarg, "{:,}".format(bz.specificitemprice(newarg))))
    except ValueError:
        await message.channel.send("Sorry, but you mistyped your item.")

@bot.command()
async def value(message, *args):
    newarg = " ".join(args)
    try:
        if bz.specificitemvalue(newarg) == -1:
            await message.channel.send("```There are currently no buy orders for {}```".format(newarg))
        else:
            await message.channel.send("```{} is worth {} coins each.```".format(newarg, "{:,}".format(bz.specificitemvalue(newarg))))
    except ValueError:
        await message.channel.send("Sorry, but you mistyped your item.")
@bot.command()
async def ahprice(message, *args):
    arg = " ".join(args)
    await message.channel.send("This may take some time...")
    msg = ah.ahPrice(arg)
    if msg[0] == "N/A" or msg[1] == -1 or msg[2] == "N/A":
        await message.channel.send("Sorry, but there are no bin auctions for {}. Or you mistyped your item name.".format(arg))
    else:
        msgstr = "The cheapest {} is {}, you can look at the auction with the command ```/viewauction {}```".format(msg[0], msg[1], msg[2])
        await message.channel.send("{}, {}".format(message.author.mention, msgstr))
@bot.command()
async def GT(message, arg):
    for i in range(len(arg)):
        if arg[i] in " `~!@#$%^&*()-_=+qwertyuiop[]asdfghjkl;'\\zxcvbnm,./QWERTYUIOP\{\}ASDFGHJKL:\"|ZXCVBNM<>?":
            await message.channel.send("Please only type the amount of coins you want to invest after $gt")
            arg = "N/A"
            break
    
    if arg != "N/A":
        TUPLE = bz.goldenTooth(int(arg))
        await message.channel.send("buy {} Wolf teeth, {} enchanted gold, and you will get {} golden teeth for a total of {} profit.".format("{:,}".format(TUPLE[0]), "{:,}".format(TUPLE[1]), "{:,}".format(TUPLE[2]), "{:,}".format(TUPLE[3])))
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
