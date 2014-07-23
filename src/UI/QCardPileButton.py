'''
Created on Jul 11, 2011

@author: mitchell
'''

from QPictureButton import QPictureButton
from PyQt4.QtCore import SIGNAL, QSize, QPropertyAnimation
from PyQt4.QtGui import QPixmap, QListView, QAbstractItemView, QWidget, QPushButton, QVBoxLayout, QLabel
import os
import pickle
from util import utilities
from UI.QCardListViewer import QCardListViewer

# TODO: Display top card on click
class QCardPileButton(QPictureButton):
    def __init__(self, parent):
        QPictureButton.__init__(self,parent)
        self.displaysTopCard = True
        self.contextMenuCallback = None
    
    def setContextMenuCallback(self, callback):
        self.contextMenuCallback = callback 
    
    def setModel(self, model):
        self.model = model
        self.connect(self.model, SIGNAL('dataChanged(QModelIndex,QModelIndex)'), self.updateTopCard)
        self.connect(self.model, SIGNAL('rowsInserted(QModelIndex,int,int)'), self.updateTopCard)
        self.connect(self.model, SIGNAL('rowsRemoved(QModelIndex,int,int)'), self.updateTopCard)
    
    def updateTopCard(self, ignored1=None, ignored2=None, ignored3=None):
        if not self.displaysTopCard:
            return
        if len(self.model.list) > 0:
            self.pixmap = self.model.list[0].pixmap()
        else:
            self.pixmap = QPixmap(os.path.join('images','empty.jpg'))
        self.repaint()
        
    def dragEnterEvent(self, event):
        event.acceptProposedAction()
    
    def dropEvent(self, event):
        data = event.mimeData()
        cardData = data.data('application/x-QCard')
        droppedCard = pickle.loads(cardData)
        index = 0
        if self.contextMenuCallback is not None:
            index = self.contextMenuCallback()
        if index == -1:
            return
        self.model.addItem(droppedCard, index)
        event.acceptProposedAction()
    
    def viewContents(self):
        QCardListViewer(self.model, self.enlargeFunction, self.window())