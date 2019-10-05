import boto3
from discord.ext import commands

class reg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        dynamodb1 =boto3.resource('dynamodb', region_name='us-west-2')
        table= dynamodb1.Table('discordpy')
        self.table=table
    
    @commands.command()
    async def reg(self, ctx):
        self.table.put_item(
            Item={
                'userid':ctx.author.id,
            }
        )
def setup(bot):
    bot.add_cog(reg(bot))