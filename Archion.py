import os
import sys
import json
import discord
from rich.console import Console
from discord.ext import commands, bridge

client = bridge.Bot(
    commands.when_mentioned_or(*"^"),
    intents=discord.Intents.all(),
    help_command=None,
    case_intensitive=True,
    debug_guilds=[guildID]) #Remove this line to get global slash commands
                            #debug_guilds is for testing the slash commands on the test Server
console = Console()

if __name__ == "__main__":
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"Cogs.{filename[:-3]}")
            console.print(filename, style="bold underline purple")
client.load_extension("jishaku")

with open("Database/Config.json", "r") as file:
    data = json.load(file)
    token = data["token"]

client.run(token)
