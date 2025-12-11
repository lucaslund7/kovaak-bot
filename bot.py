import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=">", intents=intents)

token = os.getenv('TOKEN')

guild = discord.Object(id=1391210266884309174)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.command()
async def link(ctx, arg):
    await ctx.send(arg)

client.run(token)