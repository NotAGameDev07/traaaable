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
import boykisser

TOKEN = open("TOKEN").read()
CMD_PREFIX = "&"

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents)

bot.remove_command('help')

@bot.command()
async def help(ctx):
	commands = [
		"getmeme",
		"rickroll",
		"joke",
		"filetest",
		"boykisser"
	]
	await ctx.reply(f"Available commands: {', '.join([f'`{i}`' for i in commands])}\n Do `{CMD_PREFIX}<command> help` where `<command>` is a listed command for more info on a specific command")

@bot.command()
async def getmeme(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.send("Sends a random meme from meme-api.com, specifically the title and image")
		return
	content = requests.get("https://meme-api.com/gimme").json()
	message = f"{content['title']}\n{content['url']}"
	await ctx.reply(message)

@bot.command()
async def rickroll(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.reply("Sends a rickroll gif")
		return
	await ctx.send("https://c.tenor.com/o656qFKDzeUAAAAM/rick-astley-never-gonna-give-you-up.gif")
	await asyncio.sleep(2)
	await ctx.reply("Never gonna give you up")

@bot.command()
async def joke(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.reply("Sends a random joke")
		return
	message = jokes.random_joke()
	await ctx.reply(message['Prompt'] + "\n\n" + message['Answer'] + "\n\n" + message['Credit'])

@bot.command()
async def filetest(ctx, helpflag: str = ""):
	if helpflag:
		await ctx.reply("TEST DEV CMD, sends a text file containing the bot's invite link")
		return
	await ctx.send(file=discord.File("invite_link.txt"))

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

#make sure to have your own folder of images, edit the path of the images that the script in boykisser.py searches for in boykisser.py

@bot.command(name="boykisser")
async def _boykisser(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.reply("Sends a random boykisser")
		return
	await ctx.send(file=discord.File(random.choice(boykisser.get_boykissers())))

# end of the boykissing

@bot.command()
async def homedepot(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.reply("Sends the Home Depot logo")
		return
	await ctx.send("https://corporate.homedepot.com/sites/default/files/image_gallery/THD_logo.jpg")

@bot.command()
async def seven(ctx, helpflag: str = ""):
	if helpflag == "help":
		await ctx.reply("Sends a seven")
		return
	await ctx.send("https://static.wikia.nocookie.net/halo/images/a/ac/VWNUM7.jpg/revision/latest?cb=20080312043203")

bot.run(TOKEN)