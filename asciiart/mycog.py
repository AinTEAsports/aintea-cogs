from redbot.core import commands
from selenium import webdriver

"""import webscrapGet as wG
import urlGenerator as uG"""


with open('textPolices.txt', 'r') as f:
    fontList = f.read()


def createUrl(textStyle : str, text : str):
    """Function that will create URL from style and text

    Args:
        textStyle (str): the text style you want
        text (str): the text you want to convert to ASCII art

    Returns:
        str: the URL where will be scraped the ASCII art
    """
    
    return f"https://patorjk.com/software/taag/#p=display&f={textStyle}&t={text}"


def getASCII(siteURL : str):
    """Function to get ASCII art from a link

    Args:
        siteURL (str): the link where the function will take
                        the ASCII art

    Returns:
        str: the ASCII art the program got from the website
    """

    # Setting headless mode
    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    
    driver = webdriver.Firefox(options=driverOptions)
    driver.get(siteURL)
    
    # Getting the ASCII art
    asciiArt = driver.find_element_by_id("taag_output_text")

    # If no ASCII art has been got, the program will return an empty
    # string
    if not asciiArt:
        return ""
        
    # Returns ASCII art without HTML balises
    return asciiArt.text




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
