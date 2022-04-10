import discord
import datetime
import googletrans
import pytz
from pytz import timezone as tz
from discord.ext import commands, bridge
from discord.commands import slash_command, Option

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Gives you the time of a timezone")
    async def time(self, ctx, timezone: Option(str, autocomplete=discord.utils.basic_autocomplete(pytz.all_timezones))):
        await ctx.respond(f"{timezone}, {datetime.datetime.now(tz(timezone)).strftime('%A %H:%M:%S - %d.%m.%Y')}", delete_after=60)

    @bridge.bridge_command(description="Timezonelist for the time command")
    async def timezonelist(self, ctx):
        await ctx.respond("https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568", delete_after=60)

    @slash_command(description="Translate something")
    async def translate(self, ctx, text: str, to: Option(str, autocomplete=discord.utils.basic_autocomplete(googletrans.LANGCODES))):
        to = to.lower()
        if to not in googletrans.LANGUAGES and to not in googletrans.LANGCODES:
            await ctx.respond("https://github.com/Zervyrel/Archion/blob/main/Database/Languages.txt", delete_after=60)

        else:
            x = "".join(text)
            translator = googletrans.Translator()
            text_translated = translator.translate(x, dest=to).text
            embed = discord.Embed(description=text_translated) 
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, delete_after=60)

    @bridge.bridge_command(description="Gives you the list of Languages")
    async def translate_languages(self, ctx):
        await ctx.respond("https://github.com/Zervyrel/Archion/blob/main/Database/Languages.txt", delete_after=60)

def setup(client):
    client.add_cog(Utility(client))
