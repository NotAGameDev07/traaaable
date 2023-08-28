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
CMD_PREFIX = ">"

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents)

@bot.command()
async def helpp(ctx, *command):
	commands = [
		"getmeme",
		"rickroll",
		"joke",
        "filetest",
        "boykisser"
	]
	infos = [
		"Sends a random meme from meme-api.com",
		"Sends a rickroll gif",
		"Sends a random joke",
		"Placeholder file test",
		"Sends a random boykisser gif"
	]
	if len(command) == 0:
		await ctx.send("do `>help more` for more info from help")
		await ctx.send(f"Available commands: {', '.join(commands)}")
	if command[0] == "more":
		embed = discord.Embed(
			title = "Commands:",
            description = "These are the more commands you can use",
            color = discord.Color.blue()
		)
		embed.add_field(name="Available commands:", value=f"{', '.join(commands)}")
		for (i, j) in zip(commands, infos):
			embed.add_field(name=i, value=infos, inline=False)
		embed.set_author(name="Traaaable", icon_url="https://th.bing.com/th/id/OIP.V3nxXA_MHlYrbYIyhqPpxQHaJv?pid=ImgDet&rs=1")
		await ctx.send(embed=embed)

@bot.command()
async def getmeme(ctx):
	content = requests.get("https://meme-api.com/gimme").json()
	message = f"{content['title']}\n{content['url']}"
	await ctx.send(message)

@bot.command()
async def rickroll(ctx):
	await ctx.send("https://c.tenor.com/o656qFKDzeUAAAAM/rick-astley-never-gonna-give-you-up.gif")
	await asyncio.sleep(2)
	await ctx.send("Never gonna give you up")

@bot.command()
async def joke(ctx):
	message = jokes.random_joke()
	await ctx.send(message['Prompt'] + "\n\n" + message['Answer'] + "\n\n" + message['Credit'])

@bot.command()
async def filetest(ctx):
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

#make sure to have your own folder of images, edit this in boykisser.py

@bot.command(name="boykisser")
async def _boykisser(ctx):
	await ctx.send(file=discord.File(random.choice(boykisser.get_boykissers())))

bot.run(TOKEN)