from PyQt4.QtCore import QObject, QTimer, SIGNAL
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol

import settingsManager

from ThriftDraft import TDraft

def cardToTuple(card):
    if len(card.split(',')) == 2:
        return (card.split(',')[0],card.split(',')[1])
    else:
        return card

class DraftClient(QObject):
    def __init__(self):
        QObject.__init__(self, None)
        self.transport = TSocket.TSocket(settingsManager.settings['hostname'], 42140)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = TDraft.Client(self.protocol)
        self.transport.open()

    def setUp(self, draftID, playersExpected, packNames):
        self.client.DsetUpDraft(draftID, playersExpected, packNames)
        self.draftID = draftID

    def register(self, playerName):
        self.playerID = self.client.DregisterPlayer(self.draftID, playerName)
        print "Registered with server. PlayerID is %s" % self.playerID

    def unregisterPlayer(self):
        self.client.DunregisterPlayer(self.draftID, self.playerID)

    def getAllCards(self):
        list = self.client.DgetAllCards(self.draftID)
        return [cardToTuple(card) for card in list]

    def signalReady(self):
        print "Signaling readiness (playerID is %s)..." % self.playerID
        self.client.DsignalReady(self.draftID, self.playerID)

    def everyoneReady(self):
        return self.client.DeveryoneReady(self.draftID)

    def getCurrentPack(self):
        list = self.client.DgetCurrentPack(self.draftID, self.playerID)
        return [cardToTuple(card) for card in list]

    def pickCard(self, card):
        self.client.DpickCard(self.draftID, self.playerID, "%s,%s"%(card[0],card[1]))
