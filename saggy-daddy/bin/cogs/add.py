from discord.ext import commands

class add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def add(self, ctx,arg1, arg2):
        sum = int(arg1) + int(arg2)
        await ctx.send(sum)

def setup(bot):
    bot.add_cog(add(bot))