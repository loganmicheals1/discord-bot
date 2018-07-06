import discord
from discord.ext import commands

TOKEN = 'NDY0OTEyNzk2MDQwMjk4NTE5.DiF3iQ.fdOUfO1EzbTB9t0W1q97C6GZ4gU'

description = '''bot'''
bot = commands.Bot(command_prefix='!' , description = description)


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")

