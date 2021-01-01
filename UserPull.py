import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import csv

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print('Logged on as {0.user}.'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$test'):
        await message.channel.send('present')
    if message.content.startswith('$pull'):
        # me experimenting while commands nonresponsive
        return
        server = message.guild
        await server.chunk()
        names = [member.display_name for member in server.members]

"""
This bot simply does not notice commands and I can't figure out why.
"""

@bot.command()
async def why(ctx):
    print('entered')
    await ctx.send('because')

@bot.command()
async def pull(ctx):
    server = ctx.guild
    await server.chunk()
    names = [member.display_name for member in server.members]
    print(len(names))
    print(names)

bot.run(token)
