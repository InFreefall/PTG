'''
Created on Jul 2, 2011

@author: mitchell
'''

import cardCrawler
import settingsManager
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DDraftModel(QAbstractListModel):
    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.list = []
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.list)
    
    def addItem(self, item, row=-1):
        if row is -1:
            row = len(self.list)
        self.beginInsertRows(QModelIndex(), row, row)
        self.list.insert(row, item)
        self.endInsertRows()
    
    def removeItem(self, item=None):
        row = self.list.index(item)
        self.beginRemoveRows(QModelIndex(), row, row)
        self.list.remove(item)
        self.endRemoveRows()
        
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        #if index.row() >= len(self.list):
        #    return QVariant()
        if role == Qt.DecorationRole:
            card = self.list[index.row()]
            file = os.path.join(settingsManager.settings['cardsDir'],'%s' % (card[0]),'%s.jpg' % (card[1]))
            if not os.path.isfile(file):
                cardCrawler.crawlCardAndInfo(card[0], card[1], False)
            return QPixmap(file)
        return QVariant()