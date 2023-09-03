import boykisser
import discord
import random
import asyncio
from discord.ext import commands

class Fun_Commands(commands.Cog):
	"""just some funny commands"""
	#make sure to have your own folder of images, edit the path of the images that the script in boykisser.py searches for in boykisser.py

	@commands.slash_command(name="boykisser", description="Sends a random boykisser")
	async def _boykisser(self, ctx):
		"""Sends a random boykisser"""
		await ctx.respond(file=discord.File(random.choice(boykisser.get_boykissers())))

	# end of the boykissing

	@commands.slash_command(description="Sends the Home Depot logo")
	async def homedepot(self, ctx):
		"""Sends the Home Depot logo"""
		await ctx.respond("https://corporate.homedepot.com/sites/default/files/image_gallery/THD_logo.jpg")

	@commands.slash_command(description="Sends a 7 (seven)")
	async def seven(self, ctx):
		"""Sends a 7 (seven)"""
		await ctx.respond("https://static.wikia.nocookie.net/halo/images/a/ac/VWNUM7.jpg/revision/latest?cb=20080312043203")
	
	@commands.slash_command(description="Sends a Cheeseburger")
	async def cheeseburger(self, ctx):
		pass

	@commands.slash_command(description="Sends a rickroll")
	async def rickroll(self, ctx):
		"""Sends a rickroll"""
		await ctx.send("https://c.tenor.com/o656qFKDzeUAAAAM/rick-astley-never-gonna-give-you-up.gif")
		await ctx.respond("Never gonna give you up")

def setup(bot):
	bot.add_cog(Fun_Commands(bot))