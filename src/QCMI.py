'''
Created on Jul 18, 2011

@author: mitchell
'''

from PyQt4.QtCore import QObject, SIGNAL
import pickle

interfaces = []

class ClientModelInterface(QObject):
    def __init__(self, model, client, zone):
        QObject.__init__(self)
        self.model = model
        self.client = client
        self.zone = zone
        
        self.connect(self.model, SIGNAL('rowsInserted(QModelIndex,int,int)'), self.sendAddCardTo)
        self.connect(self.model, SIGNAL('rowsRemoved(QModelIndex,int,int)'), self.sendRemoveCardFrom)
        self.connect(self.model, SIGNAL('dataChanged(QModelIndex,QModelIndex)'), self.sendSetCardTo)
        
        interfaces.append(self)
    
    def sendAddCardTo(self, parent, start, end):
        card = self.model.list[start]
        cardString = card.serialized()
        self.client.addCardTo(cardString, self.zone, start)
    
    def sendRemoveCardFrom(self, parent, start, end):
        self.client.removeCardFrom(self.zone, start)
    
    def sendSetCardTo(self, topLeft, bottomRight):
        for row in range(topLeft.row(), bottomRight.row()+1):
            pickledCard = self.model.list[row].serialized()
            self.client.setCardTo(pickledCard, self.zone, row)
