from redbot.core import commands
from selenium import webdriver

from asciiModules.webscrapGet import getASCII
from asciiModules.urlGenerator import createUrl


with open('./asciiModules/textPolices.txt', 'r') as f:
    fontList = f.read()


############ COG CLASS #############


class MyCog(commands.Cog):
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
    async def ascii_art(self, ctx, style : str, *, text : str):
        text = " ".join(text)
        
        if not text:
            await ctx.send("```\nPlease enter text```")
            return
        
        if style not in fontList:
            await ctx.send(f"```\nStyle '{style}' does not exist```")
            return
        
        url = createUrl(textStyle=style, text=text)
        asciiArt = getASCII(url)
        
        await ctx.send(f"```\n{asciiArt}```")
