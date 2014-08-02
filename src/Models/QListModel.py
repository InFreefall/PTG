'''
Created on Jul 10, 2011

@author: mitchell
'''

from PyQt4.QtCore import QAbstractListModel, QModelIndex, SIGNAL

class QListModel(QAbstractListModel):
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
    
    def setItem(self, item, index):
        self.list[index] = item
        emittedIndex = self.index(index,0)
        self.emit(SIGNAL('dataChanged(QModelIndex,QModelIndex)'),emittedIndex,emittedIndex)