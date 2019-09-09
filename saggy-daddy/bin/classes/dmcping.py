from mcstatus import MinecraftServer
from socket import timeout

class discordMCping():
    def __init__(self, ip):
        self.ip = ip
    def ping(self):
        try:
            server = MinecraftServer.lookup(self.ip)
            status = server.status()
            return status
        except timeout:
            return "Server Ded"
        
    def players(self):
        if(discordMCping(self.ip).ping() != "Server Ded"):
            status = discordMCping(self.ip).ping()
            return status.players.online
        else:
            return "Server Ded"
        
