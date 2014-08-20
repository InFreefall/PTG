'''
Created on Jul 10, 2011

@author: mitchell
'''

from Models.QListModel import QListModel
from PyQt4.QtCore import Qt, QVariant
import os
import random

class QDeckListModel(QListModel):
    def __init__(self, parent,game="Magic"):
        QListModel.__init__(self, parent)
        if game == "Magic":
            self.fileList = [file for file in os.listdir(os.path.join('src',"userdata",'decks')) if not file.startswith('.')]
        elif game == "Yu-Gi-Oh":
            self.fileList = [file for file in os.listdir(os.path.join('src','userdata','ygoDecks')) if not file.startswith('.')]
        self.fileList = [file for file in self.fileList if not file.endswith('~')]
        self.fileList.sort(key=str.lower)
        self.list = [os.path.splitext(file)[0] for file in self.fileList]
        self.list.insert(0, "Random Deck") 
    
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.list[index.row()]
        return QVariant()
    
    def fileForRow(self, row):
        row -= 1
        if row is -1:
            return random.choice(self.fileList)
        else:
            return self.fileList[row]
