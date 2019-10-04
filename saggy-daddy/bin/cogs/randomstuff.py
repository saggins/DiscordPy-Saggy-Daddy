from discord.ext import commands

class Randomstuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def add(self, ctx,arg1, arg2):
        sum = arg1 + arg2
        await ctx.send(sum)

def setup(bot):
    bot.add_cog(Randomstuff(bot))