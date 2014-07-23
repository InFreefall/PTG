'''
Created on Jul 2, 2011

@author: mitchell
'''

from threading import Thread
import time
from lobbyServer import LobbyHandler
from ThriftServer import PTGHandler
from DraftServer import DraftHandler

class ServerThread(Thread):
    def __init__(self, sClass, port, message):
        Thread.__init__(self)
        self.sClass = sClass
        self.server = self.sClass()
        self.port = port
        self.message = message
        self.daemon = True
        
    def kill(self):
        self.server.stop()
    
    def reload(self):
        pass #TODO: reload server
    
    def started(self):
        return self.server.started
    
    def run(self):
        self.server.run(self.server.service, self.port, self.message)

class ServerManager:
    def run(self):
        self.servers = {'lobby':None,
                        'game':None,
#                        'draft':None,
        }
        self.servers['lobby'] = ServerThread(LobbyHandler, 42141, "Starting lobby...")
        self.servers['game'] = ServerThread(PTGHandler, 42142, "Starting game server...")
        #self.servers['draft'] = ServerThread(DraftHandler, 42140, "Starting draft handler...")
        for server in self.servers.values():
            if server is not None:
                server.start()
        # Wait for all servers to start...
        while True:
            toBreak = True
            for server in self.servers.values():
                if not server.started():
                    toBreak = False
            if toBreak:
                break
        while True:
            print '> ',
            command = raw_input()
            parts = command.split(' ')
            if parts[0] in ("r", "restart"):
                # Restart
                if parts[1] == "all":
                    print "Restarting...."
                    for server in self.servers.values():
                        if server is not None:
                            server.kill()
                            time.sleep(2)
                            server.reload()
                            server.run()
                else:
                    server = self.servers[parts[1]]
                    server.kill()
                    time.sleep(2)
                    server.reload()
                    server.run()
            # end if parts[0] == 'r'
            if parts[0] == 's':
                # Start server
                pass
            if parts[0] in ('q', "quit", "exit"):
                break
            

if __name__ == '__main__':
    ServerManager().run()
