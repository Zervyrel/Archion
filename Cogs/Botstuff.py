import os
import sys
import psutil
import aiohttp
import discord
import datetime
from discord.ui import View, Button
from discord.ext import commands, bridge
from discord.commands import slash_command, Option

class Botinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bridge.bridge_command(description="Information about the Bot")
    async def botinfo(self, ctx):
        embed = discord.Embed(title="Bot info", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        embed.add_field(name="Servers", value=len(self.client.guilds), inline=False)
        embed.add_field(name="Users", value=len(self.client.users), inline=False)
        embed.add_field(name="Channels", value=len(self.client.channels), inline=False)
        embed.add_field(name="Library", value="[Pycord](https://github.com/Pycord-Development/pycord)", inline=False)
        embed.add_field(name="Latency", value=round(self.client.latency * 1000), inline=False)
        embed.add_field(name="Invite", value="[click me](https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=2147601408&scope=bot%20applications.commands)", inline=False)
        embed.add_field(name="Github", value="[click me](https://github.com/Zervyrel/Archion)", inline=False)
        embed.add_field(name="Developer/Owner", value="Zervyrel", inline=False)
        await ctx.respond(embed=embed, delete_after=60)

    @bridge.bridge_command(description="Information about the System")
    async def systeminfo(self, ctx):
        embed = discord.Embed(title="Systeminfo", timestamp=datetime.datetime.now())
        embed.add_field(name="CPU Cores", value=psutil.cpu_count(), inline=False)
        embed.add_field(name="CPU", value=psutil.cpu_percent(1), inline=False)
        embed.add_field(name="RAM", value=psutil.virtual_memory()[2], inline=False)
        await ctx.respond(embed=embed, delete_after=60)

    @slash_command(description="Information about the Latency/Website")
    async def ping(self, ctx, url: Option(str, required=False)):

        if url == None:
            await ctx.respond(f"Pong! {round(self.client.latency * 1000)} ms")
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get(url)

                if request.status == 200:
                    embed = discord.Embed(title="Website", url=url, timestamp=datetime.datetime.now())
                    embed.add_field(name="Status", value="Online")
                    await ctx.respond(embed=embed, delete_after=60)

                else:
                    embed = discord.Embed(title="Website", url=url, timestamp=datetime.datetime.now())
                    embed.add_field(name="Status", value="Offline")
                    await ctx.respond(embed=embed, delete_after=60)

    @bridge.bridge_command(description="Invites the Archion bot to your Server")
    async def invite(self, ctx):
        button = Button(label="Invite", url=f"https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=2147601408&scope=bot%20applications.commands")
        view = View()
        view.add_item(button)
        await ctx.respond("To invite me press the Button below this message", view=view, delete_after=60)

    @commands.command(description="Restarts the Bot")
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply("Restarting...")
        os.system("clear")
        os.execv(sys.executable, ["python"] + sys.argv)

    @commands.command(description="Shuts down the Bot")
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.reply("Shutting down...")
        exit()

def setup(client):
    client.add_cog(Botinfo(client))
