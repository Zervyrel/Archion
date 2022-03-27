import discord
import datetime
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        try:
            await guild.create_text_channel("Test")

        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        embed = discord.Embed(title=guild.name, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Roles", value=guild.roles, inline=False)
        embed.add_field(name="Members", value=len(guild.members), inline=False)
        embed.add_field(name="Channels", value=len(guild.channels), inline=False)
        embed.add_field(name="Serverid", value=guild.id, inline=False)
        embed.add_field(name="Created at", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        channel = self.client.get_channel(956987421260648488)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        embed = discord.Embed(title=guild.name, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Roles", value=guild.roles, inline=False)
        embed.add_field(name="Members", value=len(guild.members), inline=False)
        embed.add_field(name="Channels", value=len(guild.channels), inline=False)
        embed.add_field(name="Serverid", value=guild.id, inline=False)
        embed.add_field(name="Created at", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        channel = self.client.get_channel(956987421260648488)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Server(client))