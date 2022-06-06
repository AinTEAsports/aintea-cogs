import discord
from redbot.core import commands
from selenium import webdriver
from discord_slash import cog_ext

from .asciiModules.webscrapGet import get_ascii, get_font_list
from .asciiModules.urlGenerator import create_url


############ COG CLASS #############

class AsciiCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot) -> None :
        self.bot = bot



    @cog_ext.cog_slash(name="avatar", description="Get your avatar in ASCII art")
    async def avatar(self, ctx, user : discord.User = None):
        if not user:
            user = ctx.author
        
        await ctx.send(user.avatar_url)
     
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send("I'm here")
        
    
    @commands.command()
    async def ascii_art(self, ctx, style : str = "Graffiti", *text : str):
        text = " ".join(text)
        
        if not text:
            await ctx.send("```\nPlease enter text```")
            return
        
        if style not in get_font_list():
            await ctx.send(f"```\nStyle '{style}' does not exist```")
            return
        
        url = create_url(textStyle=style, text=text)
        asciiArt = get_ascii(url)
        
        await ctx.send(f"```\n{asciiArt}```")


    @commands.command()
    async def ascii_style_list(self, ctx):
        await ctx.send(f"```\n{get_font_list()}```")


