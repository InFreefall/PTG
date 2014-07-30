from Networking import gameClient as client
from card import Card
import os
import pdb
import pybonjour
import select
import sys
import threading

from HandyPTG import HandyPTG
from HandyPTG.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HandyServer(threading.Thread):
    def __init__(self, username, battle):
        threading.Thread.__init__(self)
        self.daemon = True
        name = "PTG: %s" % (username)
        regtype = "_PTG._tcp."
        port = 9429
        self.running = True
        
        print "Starting thrift server..."
        HandyThriftServer(port, battle, self).start()
        
        print "Registering DNS service"
        self.sdRef = pybonjour.DNSServiceRegister(name = name,
                                                  regtype = regtype,
                                                  port = port,
                                                  callBack = self.register_callback)
        
    
    def register_callback(self, sdRef, flags, errorCode, name, regtype, domain, otherStuff):
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print 'Registered service!'
    
    def run(self):
        try:
            while self.running:
                ready = select.select([self.sdRef],[],[])
                if self.sdRef in ready[0]:
                    pybonjour.DNSServiceProcessResult(self.sdRef)
        finally:
            self.sdRef.close()

class HandyThriftServer(threading.Thread):
    def __init__(self, port, battle, bonjourServer):
        threading.Thread.__init__(self)
        self.battle = battle
        self.port = port
        self.daemon = True
        self.bonjourServer = bonjourServer
        
    def run(self):
        handler = self
        processor = HandyPTG.Processor(handler)
        transport = TSocket.TServerSocket(self.port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        
        self.events = []
        
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        print "Starting server..."
        server.serve()
        print "Quitting"
    
    def HPTGgetEvents(self, sinceIndex):
        if (self.bonjourServer is not None):
            self.bonjourServer.running = False
            self.bonjourServer = None
        retVal = self.events[(sinceIndex+1):]
        return retVal
    
    def HPTGdrawCard(self):
        abbreviation, index = self.battle.player.drawCard(False)
        event = HPTGEvent()
        event.type = "drawCard"
        event.data = [abbreviation, index]
        self.addEvent(event)
    
    def HPTGplayCard(self, abbreviation, index):
        self.HPTGplayCardToScroller(abbreviation, index, self.battle.player.creatureScroller)
    
    def HPTGlandCard(self, abbreviation, index):
        self.HPTGplayCardToScroller(abbreviation, index, self.battle.player.landScroller)
    
    def HPTGplayCardToScroller(self, abbreviation, index, scroller):
        card = Card(abbreviation, index, delegate=self.battle.player)
        for cardInHand in self.battle.player.hand:
            if cardInHand.abbreviation == abbreviation and cardInHand.index == index:
                cardInHand.parent.removeCard(cardInHand)
                break
        scroller.addCard(card)
        self.battle.client.moveCard(card.abbreviation, card.index, client.HAND, card.position, card.tapped)
    
    def HPTGdiscardCard(self, abbreviation, index):
        card = Card(abbreviation, index, delegate=self.battle.player)
        for cardInHand in self.battle.player.hand:
            if cardInHand.abbreviation == abbreviation and cardInHand.index == index:
                cardInHand.parent.removeCard(cardInHand)
                break
        self.battle.client.moveCard(card.abbreviation, card.index, client.HAND, client.GRAVEYARD, False)
        self.battle.player.sendToGraveyard(card)
    
    def HPTGgetCard(self, abbreviation, index):
        path = os.path.join('cards', abbreviation, str(index) + ".jpg")
        file = open(path, 'r')
        card = file.read()
        file.close()
        print "Path: " + str(path)
        print "File: " + str(file)
        print "Card: " + card
        return card
    
    def addEvent(self, event):
        self.events.append(event)
        event.index = self.events.index(event)