import random
import calendar
from unidecode import unidecode

import discord
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
		phrase = " ".join(phrase)
		toReturn = ""

		transformation = {'a': '@', 'b': 'β', 'c': 'ς', 'd': 'd', 'e': '€',
						'f': 'f', 'g': 'g', 'h': 'h', 'i': '1', 'j': 'j', 'k': 'k',
						'l': 'l', 'm': 'm', 'n': 'n', 'o': '0', 'p': 'p', 'q': 'q',
						'r': 'r', 's': '§', 't': 'τ', 'u': 'µ', 'v': 'ν', 'w': 'ω',
						'x': 'χ', 'y': 'γ', 'z': 'z'
		}

		for char in phrase:
			if char in transformation.keys():
				toReturn += transformation[char]
			else:
				toReturn += char
		
		await ctx.send(f"```\n{toReturn}```")


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


	# This part doesn't work because of can't read file
	"""
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		forbiddenWords = open('./forbiddenWords.txt', 'r').read().split('\n')
		if unidecode(message.lower()) in forbiddenWords:
			await message.delete()
			await message.author.send(f"Vous ne pouvez pas envoyer ce genre de mots dans le serveur **{message.guild.name}** !")


	@commands.command()
	async def addForbiddenWord(self, ctx, word : str):
		with open('./forbiddenWords.txt', 'a') as f:
			f.write(f"\n{unidecode(word.lower())}")
		
		await ctx.message.add_reaction("✅")


	@commands.command()
	async def getForbiddenWords(self, ctx):
		forbiddenWords = open('./forbiddenWords.txt', 'r').read()

		if not forbiddenWords:
			await ctx.send("```\nAucun mot n'a été interdit sur ce serveur```")

		await ctx.send(f"```\n{forbiddenWords}```")
	"""
	

	@commands.command()
	async def sendDM(self, ctx, user : discord.User, *, text):
		text = "".join(text)

		if not isinstance(user, discord.User):
			await ctx.send(f"```\n'{user}' is not a discord user !```")
			await ctx.message.add_reaction("❌")
			return
		
		await user.send(f"```\n{text}\n\n- {ctx.author.name}```")

		await ctx.message.add_reaction("✅")
