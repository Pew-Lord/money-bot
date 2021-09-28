import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def Price(message, arg):
    pass





'''
message.author.mention (@'s the author)
message.channel.send (sends message in channel)

'''
keyfile = open("botkey.txt", "r")
botkey = keyfile.readlines()
bot.run(botkey[0])
