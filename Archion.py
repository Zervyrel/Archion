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
    debug_guilds=[903607882564636683])

if __name__ == "__main__":
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"Cogs.{filename[:-3]}")
client.load_extension("jishaku")

with open("Database/Config.json", "r") as file:
    data = json.load(file)
    token = data["token"]

@client.slash_command(description="Invites the Archion bot to your Server")
async def invite(ctx):
    button = Button(label="Invite", url=f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=2147601408&scope=bot%20applications.commands")
    view = View()
    view.add_item(button)
    await ctx.respond("To invite me press the Button below this message", view=view)

@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    exit()

@client.command()
async def restart(ctx):
    await ctx.send("Restarting...")
    os.system("clear")
    os.execv(sys.executable, ["python"] + sys.argv)

client.run(token)
