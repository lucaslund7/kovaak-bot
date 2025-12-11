import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=">", intents=intents)

token = os.getenv("TOKEN")

guild = discord.Object(id=os.getenv("TEST_ID"))

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.hybrid_command(name="test", guild=guild, description="no descs", with_app_command=True)
async def test(ctx):
    await ctx.send("This is a hybrid command!")

client.run(token)