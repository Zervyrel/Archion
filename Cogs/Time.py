import discord
import datetime
from discord.ext import commands
from pytz import timezone as timezonemodule
from Database.Timezonelist import Timezonelist
from discord.commands import slash_command, Option

class Time(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Gives you the time of a timezone")
    async def time(self, ctx, timezone: Option(str, autocomplete=discord.utils.basic_autocomplete(Timezonelist))):
        await ctx.respond(f"{timezone}, {datetime.datetime.now(timezonemodule(timezone)).strftime('%A %H:%M:%S - %d.%m.%Y')}", delete_after=20)

    @slash_command(description="Timezonelist for the time command")
    async def timezonelist(self, ctx):
        await ctx.respond("https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568", delete_after=20)

def setup(client):
    client.add_cog(Time(client))