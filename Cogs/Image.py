import os
import random
import discord
import requests
from discord.ext import commands, tasks
from discord.commands import slash_command

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Saves your image")
    async def image_save(self, ctx, attachment: discord.Attachment):
        name = "".join(attachment.url)
        if not name.endswith((".png", ".jpg", ".jepg")):
            await ctx.respond("Only png, jpg and jepg images pls", delete_after=20)
        
        else:
            response = requests.get(attachment.url)
            imagename = attachment.url.split("/")[-1]
            with open(f"Images/{imagename}", "wb") as image:
                image.write(response.content)
                image.close()
                await ctx.respond("Done!", delete_after=20)

    @slash_command(description="Saves your image")
    async def image(self, ctx):
        img = os.listdir("Images")
        random_image = random.choice(img)
        await ctx.respond(file=discord.File(f"Images/{random_image}"), delete_after=20)

def setup(client):
    client.add_cog(Image(client))
