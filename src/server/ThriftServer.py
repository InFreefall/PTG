import logging
import os
import time
import sys
sys.path.append("../gen-py")

from util import utilities
from Server import Server
from PTG import PTG
from PTG.ttypes import *

"""
Note: To install thrift, I used:
export ARCHFLAGS="-arch x86_64"
easy_install thrift

In conjunction w/ compiling the actual source code via brew
"""

LOG_FILENAME = 'ThriftServer.log'

class PTGHandler(Server):
    # Used by serverManager
    from PTG import PTG as service #@UnusedImport
    def __init__(self):
        self.playerLists = {}
        self.eventLists = {}
        self.greatestID = -1
        logging.basicConfig(level=logging.DEBUG)
    
    def registerPlayer(self, gameID, playerName, team):
        playerID = self.nextPlayerID()
        try:
            dict = self.playerLists[gameID]
        except:
            self.playerLists[gameID] = {}
            dict = self.playerLists[gameID]
        dict[playerID] = playerName
        event = Event()
        event.type = "addPlayer"
        event.data = [str(playerID), playerName, str(team)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player %s joined with id %d" % (playerName, playerID))
        return playerID

    def unregisterPlayer(self, gameID, playerID):
        del self.playerLists[gameID][playerID]
        event = Event()
        event.type = "removePlayer"
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player %d left" % (playerID))
        if len(self.playerLists[gameID]) is 0:
            del self.eventLists[gameID]
            del self.playerLists[gameID]
            return
  
    def setDeck(self, gameID, playerID, deckName, deckSize):
        event = Event()
        event.type = "setDeck"
        event.data = [str(deckName), str(deckSize)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) is using deck %s" % (playerID, deckName))
  
    def moveCard(self, gameID, playerID, abbreviation, index, originalPosition, newPosition, tapped):
        event = Event()
        event.type = "moveCard"
        event.data = [abbreviation, str(index), str(originalPosition), str(newPosition), str(tapped)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) moved card (%s,%s) from %s to %s" % (playerID, index, abbreviation, originalPosition, newPosition))
    
    def removeCardFrom(self, gameID, playerID, zone, position):
        event = Event()
        event.type = "removeCardFrom"
        event.data = [str(zone),str(position)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) removed card from %s(%s)" % (playerID, zone, position))
    
    def addCardTo(self, gameID, playerID, cardString, zone, position):
        event = Event()
        event.type = "addCardTo"
        event.data = [cardString, str(zone), str(position)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) added card to %s(%s)" % (playerID, zone, position))
    
    def setCardTo(self, gameID, playerID, cardString, zone, position):
        event = Event()
        event.type = "setCardTo"
        event.data = [cardString, str(zone), str(position)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) set card at %s(%s)" % (playerID, zone, position))
  
    def setLife(self, gameID, playerID, life):
        event = Event()
        event.type = "setLife"
        event.data = [str(life)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s)'s life changed to %d" % (playerID, life))
        
    def setPoison(self, gameID, playerID, poison):
        event = Event()
        event.type = "setPoison"
        event.data = [str(poison)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s)'s poison changed to %d" % (playerID, poison))
    
    def reveal(self, gameID, playerID, abbreviation, index):
        event = Event()
        event.type = "reveal"
        event.data = [str(abbreviation), str(index)]
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) revealed card (%s,%s)" % (playerID, abbreviation, index))
  
    def getEvents(self, gameID, sinceIndex):
        retVal = self.eventLists[gameID][(sinceIndex+1):]
        return retVal
  
    def listDecks(self, directory):
        retVal = os.listdir(os.path.join('..','userdata',directory))
        return retVal
  
    def getDeck(self, directory, deckName):
        print "retrieving deck %s" % deckName
        import os; print os.getcwd()
        try:
            print "opening %s..." % os.path.join('..','userdata',directory,deckName)
            f = open(os.path.join('..','userdata',directory,deckName), 'r')
            deck = f.read()
            f.close()
        except Exception, e:
            print "Excpetion in getDeck(%s)" % (deckName)
            print e
            deck = ""
        return deck
    
    def saveDeck(self, deckName, deck, directory):
        return
        try:
            f = open(os.path.join('..','userdata',directory,deckName), 'w')
            timestamp = "timeStamp:%s\n" % (time.time())
            f.write(timestamp)
            f.write(deck)
            f.close()
        except:
            print "Error saving deck %s" % deckName
    
    def nextPlayerID(self):
        self.greatestID += 1
        return self.greatestID

    def event(self, eventType, gameID, playerID, data):
        event = Event()
        event.type = eventType
        event.data = data
        event.sender = playerID
        self.addEvent(gameID, event)
        logging.info("Player (%s) added event of type %s" % (playerID, eventType))
    
    def addEvent(self, gameID, event):
        try:
            event.senderName = self.playerLists[gameID][event.sender]
        except:
            pass
        try:
            eventList = self.eventLists[gameID]
        except:
            eventList = []
            self.eventLists[gameID] = eventList 
        eventList.append(event)
        event.index = self.eventLists[gameID].index(event)
    
    def VERSION(self):
        return utilities.VERSION()

if __name__ == "__main__":
    server = PTGHandler()
    server.run(PTG, 42142, "Starting game server...")
