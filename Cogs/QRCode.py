import os
import qrcode
import discord
from discord.ext import commands
from qrcode.image.styles.colormasks import *
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styledpil import StyledPilImage
from discord.commands import slash_command, Option

class QRCode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Creates a QRCode with your input")
    async def qrcode(self, ctx, text: Option(str, required=True), customisation: Option(str, choices=[
        "SquareModuleDrawer",
        "GappedSquareModuleDrawer",
        "CircleModuleDrawer",
        "RoundedModuleDrawer",
        "VerticalBarsDrawer",
        "HorizontalBarsDrawer",
        "SolidFillColorMask",
        "RadialGradiantColorMask",
        "SquareGradiantColorMask",
        "HorizontalGradiantColorMask",
        "VerticalGradiantColorMask",
        "ImageColorMask"], required=False)):

        if customisation == None:
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image()
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "SquareModuleDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "GappedSquareModuleDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "CircleModuleDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "RoundedModuleDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "VerticalBarsDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "HorizontalBarsDrawer":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "SolidFillColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "RadialGradiantColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "SquareGradiantColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "HorizontalGradiantColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "VerticalGradiantColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

        elif customisation == "ImageColorMask":
            qr = qrcode.QRCode(box_size=60)
            qr.add_data(text)
            img = qr.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask())
            img.save("QRCODE.png")
            await ctx.respond(file=discord.File("QRCODE.png"), delete_after=60)
            os.remove("QRCODE.png")

    @slash_command(description="Gives you a short example")
    async def qrcode_example(
    self,
    ctx: discord.ApplicationContext):
        await ctx.respond(file=discord.File("Cogs/Images/color_masks.png"), delete_after=60)
        await ctx.respond(file=discord.File("Cogs/Images/module_drawers.png"), delete_after=60)

def setup(client):
    client.add_cog(QRCode(client))
