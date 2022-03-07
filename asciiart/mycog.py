from redbot.core import commands
from selenium import webdriver

from discord_slash import SlashCommand

from .asciiModules.webscrapGet import getASCII, getFontList
from .asciiModules.urlGenerator import createUrl


slash = SlashCommand(commands.Bot, sync_commands=True)

############ COG CLASS #############


class AsciiCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f"Hi {ctx.author.mention}")
     
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send("I'm here")
        
    
    @commands.command()
    async def ascii_art(self, ctx, style : str = "Graffiti", *text : str):
        text = " ".join(text)
        
        if not text:
            await ctx.send("```\nPlease enter text```")
            return
        
        if style not in getFontList():
            await ctx.send(f"```\nStyle '{style}' does not exist```")
            return
        
        url = createUrl(textStyle=style, text=text)
        asciiArt = getASCII(url)
        
        await ctx.send(f"```\n{asciiArt}```")


    @commands.command()
    async def ascii_style_list(self, ctx):
        await ctx.send(f"```\n{getFontList()}```")


    @slash.slash(name="avatar", description="Shows user avatar")
    async def avatar(self, ctx, user : discord.User = None):
        if not user:
            await ctx.send(ctx.author.avatar_url)
            return
        
        await ctx.send(user.avatar_url)
