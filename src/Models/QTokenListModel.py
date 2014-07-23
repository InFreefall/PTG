'''
Created on Jul 23, 2011

@author: mitchell
'''

from Models.QListModel import QListModel
from PyQt4.QtCore import Qt, QVariant
import os
import random
import settingsManager

class QTokenListModel(QListModel):
    def __init__(self, parent):
        QListModel.__init__(self, parent)
        self.fileList = [file for file in os.listdir(os.path.join(settingsManager.settings['imagesDir'], 'tokens')) if not file.startswith('.')]
        self.fileList.sort(key=str.lower)
        self.list = [os.path.splitext(file)[0] for file in self.fileList]
    
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.list[index.row()]
        return QVariant()
    
    def fileForRow(self, row):
        return self.fileList[row]