import aiohttp
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import time

PREFIX = ("$")
client = commands.Bot(command_prefix = PREFIX, description = "VITC Price")
localtime = time.asctime( time.localtime(time.time()) )
delay = int(input("How many seconds delay would you like to have (recommended 30): "))

@client.event
async def on_ready():
    while True:
        async with aiohttp.ClientSession() as session:

            api_url = "https://vitex.vite.net/api/v1/exchange-rate?tokenSymbols=VITC-000"
            print("Opening URL: success")
            async with session.get(api_url) as resp:
                api_data = await resp.json()
                data = api_data["data"]
                usdRate = data[0]["usdRate"]
                print("Waiting for " + str(delay) + " seconds to pass.....")
                # waiting
                time.sleep(delay)
                # changing status
                await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = str(usdRate) + "$"))
                print("Updated status to " + str(usdRate) + " @ " + str(localtime))

client.run("TOKEN HERE")
