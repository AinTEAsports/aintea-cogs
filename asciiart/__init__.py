from .mycog import MyCog
from .asciiModules.urlGenerator import *
from .asciiModules.webscrapGet import *

def setup(bot):
    bot.add_cog(MyCog(bot))
