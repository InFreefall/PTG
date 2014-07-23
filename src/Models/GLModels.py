'''
Created on Jun 24, 2011

@author: mitchell
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Models.QListModel import QListModel
from Models.QStringListModel import QStringListModel

class GLGameList(QListModel):
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            game = self.list[index.row()]
            inProgress = ""
            if game.started:
                inProgress = " (In Progress)"
            return game.name + " - " + game.type + inProgress
        return QVariant()
    
    def gameForID(self, gameID):
        for game in self.list:
            if game.gameID is gameID:
                return game
    
    def removeGameWithID(self, gameID):
        self.removeItem(self.gameForID(gameID))
    
class GLPlayerList(QListModel):
    def __init__(self, playerID, parent=None):
        QListModel.__init__(self, parent)
        self.myPlayerID = playerID
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.list[index.row()].playerName
        elif role == Qt.ForegroundRole and self.list[index.row()].playerID is self.myPlayerID:
            return QColor(255,0,0)
        return QVariant()
    
    def addItem(self, item, row=-1):
        if item.playerID is self.myPlayerID:
            row = 0
        QListModel.addItem(self, item, row)
    
    def playerForID(self, playerID):
        for player in self.list:
            if player.playerID is playerID:
                return player
    
    def removePlayerWithID(self, playerID):
        self.removeItem(self.playerForID(playerID))
