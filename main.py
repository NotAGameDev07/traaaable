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
import discord
import time
import asyncio
from discord.ext import commands

import jokes
import boykisser

TOKEN = open("TOKEN").read()

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

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

#make sure to have your own folder of images, edit this in boykisser.py

@bot.command()
async def boykisser(ctx):
	await ctx.send(file=discord.File(random.choice(boykisser.get_boykissers())))

bot.run(TOKEN)