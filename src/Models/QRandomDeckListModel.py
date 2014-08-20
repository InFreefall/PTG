'''
Created on May 27, 2013

This is a utility class for allowing the user to select a color for a random deck.

@author: mitchell
'''

from Models.QListModel import QListModel
from PyQt4.QtCore import Qt, QVariant

class QRandomDeckListModel(QListModel):
    def __init__(self, parent):
        QListModel.__init__(self, parent)
        self.list = ['R','U','B','W','G']
        self.mappings = {'R': "Red",
                         'U': "Blue",
                         'B': "Black",
                         'W': "White",
                         'G': "Green"}
    
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.mappings[self.list[index.row()]]
        return QVariant()
    def fileForRow(self, row):
        return self.list[row]
