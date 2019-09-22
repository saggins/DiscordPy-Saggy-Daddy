import discord 
import asyncio
import os

import sched, time

secretfile = open(os.getcwd()+"/testbot/testbot.txt", "r")
token = secretfile.read()
secretfile.close()

class testbot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
client = testbot()
client.run(token)