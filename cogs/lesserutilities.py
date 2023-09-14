""" 
/*
	* This program is free software: you can redistribute it and/or modify
	* it under the terms of the GNU General Public License as published by
	* the Free Software Foundation, either version 3 of the License, or
	* (at your option) any later version.
	*
	* This program is distributed in the hope that it will be useful,
	* but WITHOUT ANY WARRANTY; without even the implied warranty of
	* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	* GNU General Public License for more details.
	*
	* You should have received a copy of the GNU General Public License
	* along with this program. If not, see <https://www.gnu.org/licenses/>.
	*/
"""

import requests
import boykisser
import jokes
import discord
from discord.ext import commands

class Utilities(commands.Cog):
	"""Just some utility commands"""
	#make sure to have your own folder of images, edit the path of the images that the script in boykisser.py searches for in boykisser.py

	@commands.slash_command(description="Sends a random meme")
	async def meme(self, ctx):
		"""Sends a random meme"""
		content = requests.get("https://meme-api.com/gimme").json()
		message = f"{content['title']}\n{content['url']}"
		await ctx.respond(message)

	@commands.slash_command(description="Sends a random joke")
	async def joke(self, ctx):
		"""Sends a random joke"""
		message = jokes.random_joke()
		await ctx.respond(message['Prompt'] + "\n\n" + message['Answer'] + "\n\n" + message['Credit'])

	@commands.slash_command(description="Sends a file that contains the bot's invite link")
	async def filetest(self, ctx):
		"""Sends a file that contains the bot's invite link"""
		await ctx.respond(file=discord.File("invite_link.txt"))

def setup(bot):
	bot.add_cog(Utilities(bot))