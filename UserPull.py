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

@bot.command()
async def pull_users(ctx):
    server = ctx.guild
    await server.chunk()
    names = [member.display_name for member in server.members]
    with open('user_list.csv', 'w', newline='') as csvfile:
        user_writer = csv.writer(csvfile, delimiter=' ')
        for member in server.members:
            user_writer.writerow([member.display_name]) 
    outp = discord.File('user_list.csv')
    await ctx.send(file=outp)

bot.run(token)
