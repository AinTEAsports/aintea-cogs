#from redbot.core import commands

import asciiModules.webscrapGet as wG
import asciiModules.urlGenerator as uG


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
        
        if style not in wG.fontList:
            await ctx.send(f"```\nStyle '{style}' does not exist```")
            return
        
        url = uG.createUrl(textStyle=style, text=text)
        asciiArt = wG.getASCII(url)
        
        await ctx.send(f"```\n{asciiArt}```")
