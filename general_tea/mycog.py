import random
import calendar
from unidecode import unidecode

from redbot.core import commands


class TeaCog(commands.Cog):
	"""My custom cog"""

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def calendrier(self, ctx, month, year):
		try:
			month = int(month)
			year = int(year)
		except ValueError:
			await ctx.send(f"```\nParameter \"month\" ({month}) and/or parameter \"year\" ({year}) is/are invalid```")
			return
		
		if month < 1 or month > 12:
			await ctx.send(f"```\nParameter \"month\" ({month}) is invalid```")
		
		calendrierText = calendar.month(year, month)
		await ctx.send(f"```py\n{calendrierText}```")
	
	
	@commands.command()
	async def teaping(self, ctx):
		await ctx.send(f"```py\n{commands.Bot.latency()} ms```")


	@commands.command()
	async def gamerzification(self, ctx, *, phrase):

		if len(phrase) == 1:
			phrase = "".join(list(phrase))
		else:
			phrase = " ".join(list(phrase))
		lst_return = []

		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		alphabet_gamerz = ['@', 'β', 'ς', 'd', '€', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', '0', 'p', 'q', 'r', '§', 'τ', 'µ', 'ν', 'ω', 'χ', 'γ', 'z']

		for i in list(phrase):
			try:
				index = alphabet.index(i)
				if alphabet[index] == alphabet_gamerz[index]:
					lst_return.append(i)
				else:
					try:
						lst_return.append(alphabet_gamerz[index])
					except ValueError:
						lst_return.append(i)
			except ValueError:
				lst_return.append(i)

		await ctx.send("".join(lst_return))


	@commands.command()
	async def randomRename(self, ctx, user : discord.User = None):
		if not user:
			user = ctx.author
        
		nicknames = [
			'Magg Rosbit',
			'Bobby Dick',
			'Joe Mama',
			'James Labitt',
			'Jean Neymar',
			'JOHN CENA PAPALAPAAAAAA'
		]

		await user.edit(nick=random.choice(nicknames))


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		forbiddenWords = open('forbiddenWords.txt', 'r').read().split('\n')
		if unidecode(message.lower()) in forbiddenWords:
			await message.delete()
			await message.author.send(f"Vous ne pouvez pas envoyer ce genre de mots dans le serveur **{message.guild.name}** !")


	@commands.command()
	async def addForbiddenWord(self, ctx, word : str):
		with open('forbiddenWords.txt', 'a') as f:
			f.write(f"\n{unidecode(word.lower())}")
		
		await ctx.message.add_reaction("✅")
