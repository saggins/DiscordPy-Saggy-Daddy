import boto3
from discord.ext import commands

dynamodb1 =boto3.resource('dynamodb', region_name='us-west-2')
table= dynamodb1.Table('discordpy')

#TODO: Make sure to let users update/change answers
class reg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command()
    async def reg(self, ctx, *args):
        step = table.get_item(
            Key={
                'userid':ctx.author.id,
            }
        ) 

        try:
            step1=step['Item']
        except:
            await ctx.send(ctx.author.mention + " You aren't in database?. **Pls Tell server Mod!**")

        #Begining Logic
        if(step1['reg'] == 0): #Is it step 0? Name give pls
            if(len(args)!=1):
                await ctx.send('Please do $reg **Your name**')
            else:
                await self.updatestuff(ctx.author.id, 1, 'name', args[0] )
                await ctx.send('Are you part of lynbrook? $reg **yes/no**')
        
        if(step1['reg'] == 1): #Is it step 1? Give Lynbrook pls
            if(len(args)!=1 or args[0]!='yes' or args[0]!='no'):
                await ctx.send('Are you part of lynbrook? $reg **yes/no**')
            else:
                await self.updatestuff(ctx.author.id, 2, 'lynbrook', args[0] )
                await ctx.send('Do you do minecraft? Please do $reg **yes/no**')

        if(step1['reg'] == 2): #Is it step 2? Give minecraft pls
            if(len(args)!=1 or args[0]!='yes' or args[0]!='no'):
                await ctx.send('Do you do minecraft? Please do $reg **yes/no**')
            else:
                await self.updatestuff(ctx.author.id, 3, 'minecraft', args[0] )
                await ctx.send('Please do $reg **Minecraft username**')                

        if(step1['reg'] == 3): #Is it step 3? Minecraft username give pls
            if(len(args)!=3):
                await ctx.send('Please do $reg **Minecraft username**')
            else:
                await self.updatestuff(ctx.author.id, 4, 'mcname', args[0] )
                await ctx.send('Do you do minecraft? Please do $reg **yes/no**')
    
    
    
    async def updatestuff(self, id, newstep, key, value):
        table.update_item( #update reg
            Key={
                'userid': id,
            },
            UpdateExpression='SET reg = :vali1',
            ExpressionAttributeValues={
                ':vali1': newstep
            }
        )     
        table.update_item(
            Key={
                'userid': id,
            },
            UpdateExpression='SET #key = :vali1',
            ExpressionAttributeNames={
                '#key' : key
            },
            ExpressionAttributeValues={
                ':vali1': value,
            }
        )     
def setup(bot):
    bot.add_cog(reg(bot))