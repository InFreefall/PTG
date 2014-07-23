import notificationCenter
import os
import pdb
import sys
import time
sys.path.append('gen-py')

from PTG import PTG
from PTG.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

HAND=-1
DECK=-2
GRAVEYARD=-3
EXILE=-4
TOKEN=-5

class Client:
    def __init__(self, delegate, gameID=-1):
        self.transport = TSocket.TSocket('maxthelizard.doesntexist.com', 42142)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = PTG.Client(self.protocol)
        self.transport.open()
        self.lastEventIndex = -1
        self.delegate = delegate
        notificationCenter.addObserver(self, self.tapCard, "tapCard")
        if gameID is -1:
            self.gameID = int(sys.argv[1])
        else:
            self.gameID = gameID
    
    def addToBattle(self, username):
        self.playerID = self.client.registerPlayer(self.gameID, username)
        self.username = username
    
    def setDeck(self, deckName, deckSize):
        self.client.setDeck(self.gameID, self.playerID, deckName, int(deckSize))
    
    def moveCard(self, abbreviation, index, originalPosition, newPosition, tapped=False):
        self.client.moveCard(self.gameID, self.playerID, abbreviation, str(index), int(originalPosition), int(newPosition), tapped)
    
    def tapCard(self, card):
        self.moveCard(card.abbreviation, card.index, card.position, card.position, card.tapped)
    
    def setLife(self, life):
        self.client.setLife(self.gameID, self.playerID, int(life))
    
    def reveal(self, abbreviation, index):
        self.client.reveal(self.gameID, self.playerID, abbreviation, index)
    
    def update(self):
        events = self.client.getEvents(self.gameID, self.lastEventIndex)
        self.lastEventIndex += len(events)
        for event in events:
            # Process event
            if event.sender == self.playerID:
                continue
            if event.type == "addPlayer":
                self.delegate.registerPlayer(event.sender, event.data[1])
            if event.type == "removePlayer":
                self.delegate.unregisterPlayer(event.sender)
            elif event.type == "moveCard":
                self.delegate.moveCard(event.sender, event.data[0], event.data[1], int(event.data[2]), int(event.data[3]), event.data[4] == "True")
            elif event.type == "setDeck":
                self.delegate.setDeck(event.sender, event.data[0], int(event.data[1]))
            elif event.type == "setLife":
                self.delegate.setPlayerLife(event.sender, int(event.data[0]))
            elif event.type == "reveal":
                self.delegate.revealCard(event.data[0], event.data[1], event.senderName)
    
    def syncDecks(self):
        localDecks = os.listdir(os.path.join('src',"userdata",'decks'))
        remoteDecks = self.client.listDecks()
        for ld in localDecks:
            if ld in ("Draft"):
                continue
            f = open(os.path.join('src','userdata','decks', ld), 'r')
            line = f.readline()
            if line.startswith('timeStamp:'):
                f.close()
                continue
            f.seek(0)
            self.client.saveDeck(ld, f.read())
            f.close()
        for rd in remoteDecks:
            deckContents = self.client.getDeck(rd)
            try:
                f = open(os.path.join('src','userdata','decks', rd), 'r')
                firstLine = f.readline()
                f.close()
                if not firstLine.startswith('timeStamp:'):
                    # Don't overwrite a non-timestamped deck
                    continue
                localTime = float(firstLine.split(':')[-1])
                serverTime = float(deckContents.split('\n')[0].split(":")[-1])
                if serverTime > localTime:
                    f = open(os.path.join('src','userdata','decks', rd), 'w')
                    f.write(deckContents)
                    f.close()
            except:
                f = open(os.path.join('src','userdata','decks', rd), 'w')
                f.write(deckContents)
                f.close()
    
    def disconnect(self):
        try:
            self.client.unregisterPlayer(self.playerID)
            self.transport.close()
            self.client = None
            print "Disconnected"
        except:
            pass
    
    def VERSION(self):
        return self.client.VERSION()