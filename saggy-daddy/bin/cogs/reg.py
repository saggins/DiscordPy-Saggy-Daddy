import boto3
from discord.ext import commands

dynamodb1 =boto3.resource('dynamodb', region_name='us-west-2')
table= dynamodb1.Table('discordpy')

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

        if(step1['step']==0):
            if(len(args)!=1):
                await ctx.send('Please do $reg **Your name**')
            else:
                pass
                #TODO: Finish the logic system for regestration
            
def setup(bot):
    bot.add_cog(reg(bot))