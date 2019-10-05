import discord 
import asyncio
import os

secretfile = open(os.getcwd()+"/testbot/testbot.txt", "r")
token = secretfile.read()
secretfile.close()

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
client.run(token)