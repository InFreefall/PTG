'''
Created on Jul 10, 2011

@author: mitchell
'''

from PyQt4.QtCore import Qt, QVariant
from Models.QListModel import QListModel

class QStringListModel(QListModel):
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.list[index.row()]
        return QVariant()