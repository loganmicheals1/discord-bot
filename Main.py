import discord
from datetime import time
import asyncio
from datetime import datetime
from threading import Timer
from discord.ext import commands

TOKEN = 'NDY0OTEyNzk2MDQwMjk4NTE5.DiF3iQ.fdOUfO1EzbTB9t0W1q97C6GZ4gU'

description = '''bot'''
bot = commands.Bot(command_prefix='!', description=description)

client = discord.Client()


async def my_background_task():
    await bot.wait_until_ready()

    channel = discord.Object(id='427853885437247499')
    while True:
        while datetime.now().hour == 16 and datetime.now().minute == 20 or datetime.now().hour == 4 and datetime.now().minute == 20:
            await bot.send_message(channel, "The Current Time is: 4:20... NICE")
            await asyncio.sleep(60)


@bot.command()
async def schedule():
    """Says world"""

    channel = discord.Object(id='427853885437247499')
    await bot.say("Streams take place on mondays, wednesdays, and fridays from 3:30 pm until 11 pm")
    await bot.send_message(channel, "hello")


@bot.command()
async def channel():
    await bot.say("https://www.twitch.tv/blizbo_babkins")


bot.loop.create_task(my_background_task())
bot.run(TOKEN)
