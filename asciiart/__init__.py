from .mycog import AsciiCog
from .asciiModules.urlGenerator import *
from .asciiModules.webscrapGet import *

def setup(bot):
    bot.add_cog(AsciiCog(bot))
