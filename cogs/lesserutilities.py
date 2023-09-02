import requests
import boykisser
import discord
from discord.ext import commands

class Utilities(commands.Cog):
	"""Just some utility commands"""
	#make sure to have your own folder of images, edit the path of the images that the script in boykisser.py searches for in boykisser.py

	@commands.command()
	async def getmeme(self, ctx):
		"""Sends a random meme"""
		content = requests.get("https://meme-api.com/gimme").json()
		message = f"{content['title']}\n{content['url']}"
		await ctx.reply(message)

	@commands.command()
	async def joke(self, ctx):
		"""Sends a random joke"""
		message = jokes.random_joke()
		await ctx.reply(message['Prompt'] + "\n\n" + message['Answer'] + "\n\n" + message['Credit'])

	@commands.command()
	async def filetest(self, ctx):
		"""Sends a file that contains the bot's invite link"""
		await ctx.send(file=discord.File("invite_link.txt"))

def setup(bot):
	bot.add_cog(Utilities(bot))