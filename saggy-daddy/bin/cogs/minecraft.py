from discord.ext import commands
import boto3

class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    def minecraft():
    