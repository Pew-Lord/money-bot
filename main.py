import discord
from discord.ext import commands
import bzpricesfunctions as bz

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def Price(message, arg):
    pass

@bot.command()
async def Items(message, arg):
    message.channel.send(str(bz.itemnames()))



'''
message.author.mention (@'s the author)
message.channel.send (sends message in channel)
'''
keyfile = open("botkey.txt", "r")
botkey = keyfile.readlines()
bot.run(botkey[0])