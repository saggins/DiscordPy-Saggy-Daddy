import discord 
import asyncio
import os

import sched, time

secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

class SaggyDaddy(discord.Client):
    #wipe server status channel
    # send the is it  up message
    # perodxly wipe and write new message if things have changed

    async def on_ready(self):
        
        #purge server status
        channel = discord.utils.get(client.get_all_channels(), guild__name='Team Speak', name='server-status')
        print('Logged on as {0}!'.format(self.user))
        await channel.purge() 
        #server satuts checking every few minutes   
 #       s = sched.scheduler(time.time, time.sleep)
    

client = SaggyDaddy()
client.run(token)