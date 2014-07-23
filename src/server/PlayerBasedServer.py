'''
Created on Jul 2, 2011

@author: mitchell
'''
from EventBasedServer import EventBasedServer
import logging

class PlayerBasedServer(EventBasedServer):
    def __init__(self, playerClass, eventClass):
        EventBasedServer.__init__(self)
        self.players = {}
        self.greatestPlayerID = -1
        self.playerC = playerClass
        self.eventC = eventClass
    
    def registerPlayer(self, playerName):
        playerID = self.nextPlayerID()
        player = self.playerC()
        player.playerID = playerID
        player.playerName = playerName
        player.currentGameID = -1 # In Lobby
        self.players[playerID] = player
        logging.info("Player %s joined with id %d" % (playerName, playerID))
        
        e = self.eventC()
        e.type = "addPlayer"
        e.data = [playerName]
        e.sender = playerID
        self.addEvent(e)
        return playerID
    
    def unregisterPlayer(self, playerID):
        e = self.eventC()
        e.type = "removePlayer"
        e.data = []
        e.sender = playerID
        self.addEvent(e)
        
        del self.players[playerID]
        logging.info("Player %d left" % (playerID))
    
    def getPlayers(self):
        return self.players.values()
    
    def nextPlayerID(self):
        self.greatestPlayerID += 1
        return self.greatestPlayerID