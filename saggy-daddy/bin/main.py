import discord 
import asyncio
import os
from discord.ext import commands
import sched, time

secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

class SaggyDaddy(discord.Client):
    #wipe server status channel
    # send the is it  up message
    # perodxly wipe and write new message if things have changed
    def get_role(self, role_name, server):
        for role in server.roles:
            if role.name == role_name:
                return role
        
        return None

    async def on_ready(self):
        
        #purge server status
        channel = discord.utils.get(client.get_all_channels(), guild__name='Team Speak Dev', name='server-status')
        print('Logged on as {0}!'.format(self.user))
        await channel.purge() 
        #server satuts checking every few minutes   
 #       s = sched.scheduler(time.time, time.sleep)
    async def on_member_join(self, member):
        
        # Start of Beggining user stuff
        
        if(member.bot): #check if incoming user is a bot
            print("its a bot")
        else:
        # Change role of the user
            role = self.get_role("RIncomplete",member.guild)
            await member.add_roles( role)
            await member.create_dm()
            print ("member joined")
            member.channel.send(
            """
            Please use ^reg **YOUR NAME**
            """)


    async def on_message(self, message):
        #check if message is bot
        if(message.author == self.user):
            return
    bot = commands.Bot(command_prefix='^')

    @bot.command()
    async def reg(self, ctx):
        pass
        
    bot.add_command(reg)

        
        
    

client = SaggyDaddy()
client.run(token)