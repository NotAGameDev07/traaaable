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
from discord import Option

import jokes

TOKEN = open("TOKEN").read()
CMD_PREFIX = "/"

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents, debug_guilds=[835505638318276648])

bot.remove_command('help')

cogslist = [
	"lesserutilities",
	"funcommands",
]

for cog in cogslist:
	bot.load_extension(f"cogs.{cog}")

@bot.slash_command(description="Reloads all modules")
@commands.is_owner()
async def reload_cogs(ctx):
	"""Reloads all modules"""
	global bot
	for cog in cogslist:
		bot.reload_extension(f"cogs.{cog}")
		await ctx.send(f"Successfully reloaded `cogs.{cog}`!")

print(bot.commands)

@bot.slash_command(name="help", description="Get some help.")
async def help(ctx, args: Option(str, required=False)):
	help_embed = discord.Embed(title="My Bot's Help!")
	command_names_list = [x.name for x in bot.commands]
	if not args:
		help_embed.add_field(
			name="List of supported commands:",
			value="\n".join([str(i+1)+". "+x.name for i,
						x in enumerate(bot.commands)]),
			inline=False
		)
		help_embed.add_field(
			name="Details",
			value="Type `/help <command name>` for more details about each command.",
			inline=False
		)

	elif args in command_names_list:
		help_embed.add_field(
			name=args,
			value=bot.get_command(args).description
		)
	else:
		help_embed.add_field(
			name="Oh, no!",
			value="I didn't find command :("
		)
	await ctx.respond(embed=help_embed)

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