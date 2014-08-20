'''
Created on Jul 10, 2011

@author: mitchell
'''

from Models.QListModel import QListModel
from PyQt4.QtCore import Qt, QVariant, QMimeData, QModelIndex, SIGNAL
from PyQt4.QtGui import QTransform, QMenu, QAction
import pickle

class QCardModel(QListModel):
    def __init__(self, parent, controllable, preferredCardHeight=170):
        QListModel.__init__(self, parent)
        self.controllable = controllable
        self.preferredCardHeight = preferredCardHeight
    
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DecorationRole:
            card = self.list[index.row()]
            pixmap = card.pixmap()
            pixmap = pixmap.scaledToHeight(self.preferredCardHeight)
            if card.tapped:
                transform = QTransform()
                transform.rotate(90)
                pixmap = pixmap.transformed(transform)
            return pixmap
            
        return QVariant()
    
    def toggleCardAtIndexTapped(self, index):
        card = self.list[index.row()]
        self.setCardAtIndexTapped(index, not card.tapped)
    
    def setCardAtIndexTapped(self, index, tapped):
        self.setCardAtRowTapped(index.row(), tapped)
    
    def setCardAtRowTapped(self, row, tapped):
        card = self.list[row]
        card.tapped = tapped
        self.setItem(card, row)
    
    def setCardAtIndexUpsideDown(self, index, upsideDown):
        self.setCardAtRowUpsideDown(index.row(), upsideDown)
    
    def setCardAtRowUpsideDown(self, row, upsideDown):
        card = self.list[row]
        card.upsideDown = upsideDown
        self.setItem(card, row)
    
    def flipCardAtIndex(self, index):
        self.flipCardAtRow(index.row())
    
    def flipCardAtRow(self, row):
        self.setCardAtRowUpsideDown(row, not self.list[row].upsideDown)
    
    def untapAll(self):
        for i in range(0,len(self.list)):
            self.setCardAtRowTapped(i,False)
    
    def supportedDropActions(self):
        if self.controllable:
            return Qt.MoveAction
        return Qt.IgnoreAction
    def supportedDragActions(self):
        if self.controllable:
            return Qt.MoveAction
        return Qt.IgnoreAction
    
    def flags(self,index):
        defaultFlags = QListModel.flags(self,index)
        if (index.isValid()):
            return Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | defaultFlags
        return Qt.ItemIsDropEnabled | defaultFlags
    
    def dropMimeData(self, data, action, row, column, parent):
        cardData = data.data('application/x-QCard')
        droppedCard = pickle.loads(cardData)
        self.addItem(droppedCard, row)
        return True
    
    def removeRows(self, row, count, parent):
        for i in range(row,row+count):
            self.removeItem(self.list[i])
        return True
    
    def mimeData(self, indexes):
        if len(indexes) == 0:
            return 0
        index = indexes[0]
        card = self.list[index.row()]
        string = pickle.dumps(card)
        result = QMimeData()
        result.setData('application/x-QCard', string)
        return result
    
    def mimeTypes(self):
        return ['application/x-QCard']
    
    def contextMenuFunction(self, listView, player, gameDialog, parent):
        def flipSelected():
            for index in listView.selectedIndexes():
                self.flipCardAtIndex(index)
        def exileSelected():
            for index in listView.selectedIndexes():
                card = self.list[index.row()]
                self.removeItem(card)
                player.exileModel.addItem(card)  # Might have to be parent.exileModel - not sure
        def peekAtSelected():
            for index in listView.selectedIndexes():
                card = self.list[index.row()]
                self.enlargeFunction(card,flipped=True)
        def addPlusOneSelected():
            for index in listView.selectedIndexes():
                card = self.list[index.row()]
                card.addPlusOne()
                self.setItem(card, index.row())
        def removePlusOneSelected():
            for index in listView.selectedIndexes():
                card = self.list[index.row()]
                card.removePlusOne()
                self.setItem(card, index.row())
        def displayContextMenu(pt):
            menu=QMenu(parent)
            menu.addAction("+1/+1",addPlusOneSelected)
            menu.addAction("-1/-1",removePlusOneSelected)
            menu.addAction("Flip",flipSelected)
            cardIsFlipped = False
            for index in listView.selectedIndexes():
                if self.list[index.row()].upsideDown:
                    cardIsFlipped = True
            if cardIsFlipped:
                menu.addAction("Peek",peekAtSelected)
            menu.addAction("Exile",exileSelected)
            # self.generateGiveToList(menu, player, gameDialog)
            # TODO: Solve bug related to ^ line
            menu.exec_(listView.mapToGlobal(pt))
        return displayContextMenu

    def generateGiveToList(self, menu, currentPlayer, gameDialog):
        base = QAction("Give To",self)
        print gameDialog.players
        for player in gameDialog.players:
            QAction(player.name,base)
        return base
        
