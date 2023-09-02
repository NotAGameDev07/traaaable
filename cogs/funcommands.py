import boykisser
import discord
from discord.ext import commands

class Fun_Commands(commands.Cog):
	"""just some funny commands"""
	#make sure to have your own folder of images, edit the path of the images that the script in boykisser.py searches for in boykisser.py

	@commands.command(name="boykisser")
	async def _boykisser(ctx):
		"""Sends a random boykisser"""
		await ctx.send(file=discord.File(random.choice(boykisser.get_boykissers())))

	# end of the boykissing

	@commands.command()
	async def homedepot(self, ctx):
		"""Sends the Home Depot logo"""
		await ctx.send("https://corporate.homedepot.com/sites/default/files/image_gallery/THD_logo.jpg")

	@commands.command()
	async def seven(self, ctx):
		"""Sends a 7 (seven)"""
		await ctx.send("https://static.wikia.nocookie.net/halo/images/a/ac/VWNUM7.jpg/revision/latest?cb=20080312043203")

	@commands.command()
	async def rickroll(self, ctx):
		"""Sends a rickroll"""
		await ctx.send("https://c.tenor.com/o656qFKDzeUAAAAM/rick-astley-never-gonna-give-you-up.gif")
		await asyncio.sleep(2)
		await ctx.reply("Never gonna give you up")

def setup(bot):
	bot.add_cog(Fun_Commands(bot))