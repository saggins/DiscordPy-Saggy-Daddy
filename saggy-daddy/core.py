import discord 
import asyncio
import os
import Dmcping
import sched, time

secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

class SaggyDaddy(discord.Client):
    #wipe server status channel
    # send the is it  up message
    # perodxly wipe and write new message if things have changed
    async def on_ready(self):
        
        channel = discord.utils.get(client.get_all_channels(), guild__name='Team Speak', name='server-status')
        
        print('Logged on as {0}!'.format(self.user))
        lastmessage= await channel.fetch_message(channel.last_message_id)
        print( lastmessage)
 #       s = sched.scheduler(time.time, time.sleep)

client = SaggyDaddy()
client.run(token)