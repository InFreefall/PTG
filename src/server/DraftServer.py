'''
Created on Jul 3, 2011

@author: mitchell
'''
import logging
import pdb
import sys
from PlayerBasedServer import PlayerBasedServer
sys.path.append('../gen-py')

from ThriftDraft import TDraft
from ThriftDraft.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

LOG_FILENAME = 'DraftServer.log'

class DraftHandler(PlayerBasedServer):
    from ThriftDraft import TDraft as service
    def __init__(self):
        PlayerBasedServer.__init__(self, DPlayer, DEvent)
        logging.basicConfig(level=logging.DEBUG)
        self.canJoin = True
    
    def DstartDraft(self):
        self.canJoin = False
    
    def DregisterPlayer(self, playerName):
        return self.registerPlayer(playerName)

    def DunregisterPlayer(self, playerID):
        self.unregisterPlayer(playerID)
    
    def DgetPlayers(self):
        return self.getPlayers()
    
    def DcurrentEventIndex(self):
        return self.currentEventIndex()
    
    def DgetEvents(self, sinceIndex):
        return self.getEvents(sinceIndex)
    
    def DpassExpansion(self, playerID, expansion, onLeft):
        e = DEvent()
        e.type = "expansionPassedTo"
        e.sender = playerID
        e.data[0] = expansion
        if onLeft:
            newPlayerID = self.DplayerLeftOf(playerID)
        else:
            newPlayerID = self.DplayerRightOf(playerID)
        e.data[1] = newPlayerID
        self.addEvent(e)
    
    def DplayerLeftOf(self, player):
        keys = self.players.keys()
        index = keys.index(player) - 1
        if (index < 0):
            index += len(keys)
        return keys[index]
    
    def DplayerRightOf(self, player):
        keys = self.players.keys()
        index = keys.index(player) - 1
        if (index >= len(keys)):
            index -= len(keys)
        return keys[index]
    
    def DsetExpansions(self, expansions):
        e = DEvent()
        e.type = "setExpansions"
        e.data = expansions
        self.addEvent(e)

if __name__ == "__main__":
    server = DraftHandler()
    server.run(TDraft, 42140, "Starting draft server...")