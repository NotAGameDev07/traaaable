from Wordle.wordle import wordle

import discord
import random
import requests
import asyncio
from discord.ext import commands

def getword():
	return requests.get("https://random-words-api.vercel.app/word").json()[0]['word'].lower()

def correct(self, stri):
	return f"Y{stri}"

def isthere(self, stri):
	return f"M{stri}"

def incorrect(self, stri):
	return f"N{stri}"

players = dict()

class wordle(commands.Cog):
	@commands.slash_command(description="Starts a wordle game")
	async def start_wordle(self, ctx):
		players[ctx.author.id] = wordle(getword())

	@commands.slash_command(description="Enters a word into a wordle game")
	async def enter_wordle(self, ctx):
		pass