import calendar

from redbot.core import commands


class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calendrier(self, ctx, month : int, year : int) -> None:
        if not isinstance(month, int) or not isinstance(year, int):
            return
        
        if month < 1 or month > 12:
            await ctx.send(f"```\nParameter \"month\" ({month}) is invalid```")
        
        calendrierText = calendar.month(year, month)
        await ctx.send(f"```py\n{calendrierText}```")
    
    
    @commands.command()
    async def teaping(self, ctx):
        await ctx.send(f"```py\n{commands.bot.latency*1000} ms```")
