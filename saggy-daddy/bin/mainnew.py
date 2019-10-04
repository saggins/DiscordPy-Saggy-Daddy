import discord
from discord.ext import commands

import asyncio
import os
import sched, time
import sys
import traceback

import boto3

#Discord API key
secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

# Aws stuff
dynamodb1 = boto3.resource("dynamodb")
table= dynamodb1.Table('discordpy')

INITIAL_EXTENSIONS=[
    'cogs.randomstuff',
    'cogs.add',
    'cogs.reg',
]

class SaggyDaddy(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$",
                         description="stuff" )
        self.client_id=526954549638856735
        self.owner_id=185918091685920768
        self.token = token

        for extension in INITIAL_EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e:
                print('Failed to load extension {}\n{}: {}'.format(
                    extension, type(e).__name__, e))


    #async def on_command_error(self, ctx, error):
    #    print("error")
    #    await ctx.send("Ye did it wrong")
    
    async def get_role(self, role_name, server):
        for role in server.roles:
            if role.name == role_name:
                return role
        
        return None

    async def on_ready(self):
        #purge server status
        channel = discord.utils.get(self.get_all_channels(), guild__name='Team Speak Dev', name='server-status')
        print('Logged on as {0}!'.format(self.user))
        await channel.purge() 
    def putplayer(self, id):
        table.put_item(
            Item={
                'userid':id,
                'setp':0,
            }
        )
    
    async def on_member_join(self, member):
        # Start of Beggining user stu
        if(member.bot): #check if incoming user is a bot
            print("its a bot")
            chan = discord.utils.get(self.get_all_channels(), guild__name='Team Speak Dev', name='reg')
            await chan.send( member.mention + ' Please use "^reg **YOUR NAME**"')
            
        else:
        # Change role of the user
            chan = discord.utils.get(self.get_all_channels(), guild__name='Team Speak Dev', name='reg')
            await chan.send( member.mention + ' Please use "^reg **YOUR NAME**"')
            role = self.get_role("RIncomplete",member.guild)
            await member.add_roles( role)
            await member.create_dm()
            print ("member joined")
        #Put in DB
            table.put_item(Item={
                'item_id':member.id,
            })


    def run(self):
        super().run(self.token, reconnect=True)


if(__name__== "__main__"):
    saggydaddy = SaggyDaddy()
    saggydaddy.run()

