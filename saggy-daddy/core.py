import discord 
import asyncio
import os

secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

class SaggyDaddy(discord.Client):
    @asyncio.coroutine
    def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

client = SaggyDaddy()
client.run(token)