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

import random
import requests
import discord
import time
import asyncio
from discord.ext import commands

import jokes

TOKEN = open("TOKEN").read()
CMD_PREFIX = "/"

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents, debug_guilds=[835505638318276648])


cogslist = [
	"lesserutilities",
	"funcommands",
]

for cog in cogslist:
	bot.load_extension(f"cogs.{cog}")

@bot.command(description="Reloads all modules")
@commands.is_owner()
async def reload_cogs(ctx):
	"""Reloads all modules"""
	global bot
	for cog in cogslist:
		bot.reload_extension(f"cogs.{cog}")
		await ctx.send(f"Successfully reloaded `cogs.{cog}`!")

# this right here works, but is disabled for now

""" 
@bot.listen()
async def on_message(message):
	if str(message.content).startswith(CMD_PREFIX):
		return
	if message.author == bot.user:
		return
	print(message.content)
	await message.channel.send(message.content)
 """

bot.run(TOKEN)