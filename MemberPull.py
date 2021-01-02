import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import csv
import datetime

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print('Logged on as {0.user}.'.format(bot))

@bot.command()
async def pull_members(ctx):
    server = ctx.guild
    await server.chunk()
    names = [member.display_name for member in server.members]
    with open('member_list.csv', 'w', newline='') as csvfile:
        user_writer = csv.writer(csvfile, delimiter=' ')
        for member in server.members:
            user_writer.writerow([member.display_name]) 
    outfile = discord.File('member_list.csv')
    now = datetime.datetime.utcnow()
    nowstring = now.strftime('%H:%M, %m/%d/%y (UTC).')
    outstring = 'Members of {0} at '.format(server) + nowstring
    await ctx.send(content=outstring, file=outfile)

bot.run(token)
