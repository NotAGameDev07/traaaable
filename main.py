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