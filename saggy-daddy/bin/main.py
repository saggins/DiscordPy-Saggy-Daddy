import discord 
import asyncio
import os
from discord.ext import commands
import sched, time
import boto3
from boto3.dynamodb.conditions import Key, Attr 

#Discord API key
secretfile = open(os.getcwd()+"/saggy-daddy/secretstuff.txt", "r")
token = secretfile.read()
secretfile.close()

#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb1 =boto3.resource('dynamodb', region_name='us-west-2')
table= dynamodb1.Table('discordpy')


bot= commands.Bot(command_prefix='$')    



#wipe server status channel
# send the is it  up message
# perodxly wipe and write new message if things have changed

@bot.event
async def get_role(self, role_name, server):
    for role in server.roles:
        if role.name == role_name:
            return role
    
    return None

@bot.event
async def on_ready():
    
    #purge server status
    channel = discord.utils.get(bot.get_all_channels(), guild__name='Team Speak Dev', name='server-status')
    print('Logged on as {0}!'.format(bot.user))
    await channel.purge() 
    
def putplayer(id):
    table.put_item(
        Item={
            'userid':id,
            'setp':0,
        }
)

@bot.event
async def on_member_join(member, self):
    
    # Start of Beggining user stuff
    
    if(member.bot): #check if incoming user is a bot
        print("its a bot")
        chan = discord.utils.get(bot.get_all_channels(), guild__name='Team Speak Dev', name='reg')
        await chan.send( member.mention + ' Please use "^reg **YOUR NAME**"')
        
    else:
    # Change role of the user
        chan = discord.utils.get(bot.get_all_channels(), guild__name='Team Speak Dev', name='reg')
        await chan.send( member.mention + ' Please use "^reg **YOUR NAME**"')
        

        role = self.get_role("RIncomplete",member.guild)
        await member.add_roles( role)
        await member.create_dm()
        print ("member joined")
       

@commands.command()
async def add(ctx, a: int, b: int):
    print(a+b)
    await ctx.send(a + b)
@commands.command()
async def reg(ctx,arg):
    pass

bot.add_command(add)
bot.run(token)