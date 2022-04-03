import os
import sys
import json
import discord
from discord.ext import commands
from discord.ui import View, Button

client = commands.Bot(
    commands.when_mentioned_or(*"^"),
    intents=discord.Intents.all(),
    help_command=None,
    case_intensitive=True,
    debug_guilds=[903607882564636683]) #Remove this line to get global slash commands
                                       #debug_guilds if for testing the slash commands on the test Server

if __name__ == "__main__":
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"Cogs.{filename[:-3]}")
client.load_extension("jishaku")

with open("Database/Config.json", "r") as file:
    data = json.load(file)
    token = data["token"]

client.run(token)
