import discord 

secretfile = open("secretstuff.txt", "r")
token = secretfile.read(0)
secretfile.close()

class SaggyDaddy(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

client = SaggyDaddy()
client.run(token)