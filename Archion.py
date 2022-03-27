import os
import json
import discord
from discord.ext import commands, tasks

client = commands.Bot(
    commands.when_mentioned_or(*"."),
    intents=discord.Intents.all(),
    help_command=None,
    case_intensitive=True)

if __name__ == "__main__":
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"Cogs.{filename[:-3]}")
client.load_extension("jishaku")

with open("Database/Config.json", "r") as file:
    data = json.load(file)
    token = data["token"]

client.run(token)
