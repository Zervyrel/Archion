import os
import random
import discord
import requests
from discord.ext import commands, tasks
from discord.commands import slash_command

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.test_task.start()

    @slash_command()
    async def image_save(self, ctx, attachment: discord.Attachment):
            response = requests.get(attachment.url)
            imagename = attachment.url.split("/")[-1]
            with open(f"Images/{imagename}", "wb") as image:
                image.write(response.content)
                image.close()
                await ctx.respond("Done!", delete_after=20)

    @slash_command()
    async def image(self, ctx):
        img = os.listdir("Images")
        random_image = random.choice(img)
        await ctx.respond(file=discord.File(f"Images/{random_image}"), delete_after=20)

    @tasks.loop(seconds=20)
    async def test_task(self):
        for images in os.listdir("images"):
            if not images.endswith((".png", ".jpg", ".jepg")):
                os.remove(f"Images/{images}")

    @test_task.before_loop
    async def before_test_task(self):
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(Image(client))