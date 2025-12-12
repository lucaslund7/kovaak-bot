import discord
from discord.ext import commands
from discord import app_commands
import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=">", intents=intents)

path = Path("data.json")
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_guild_join(guild):
    name = guild.name
    id = str(guild.id)
    print("Joined guild '" + name + "' Id: " + id)
    if id not in data:
        data[id] = {
            "server_name": name,
            "guild_id": id,
            "links": {}
        }
        save_data()


@client.command()
async def link(ctx, arg):
    await ctx.send(arg)

def check_data():
    if path.exists():
        print("Data file found")
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    else:
        print("Data file not found, created file")
        path.write_text("{}", encoding="utf-8")
        return {}

def save_data():
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print("Saved data")

data = check_data()
client.run(token)