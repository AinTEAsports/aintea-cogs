from unidecode import unidecode

from .mycog import TeaCog

def setup(bot):
    bot.add_cog(TeaCog(bot))
