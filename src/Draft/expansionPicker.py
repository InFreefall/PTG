#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_expansionPickerUI import Ui_ExpansionPicker
from util import utilities
import sys

class ExpansionPickerModel(QAbstractListModel):
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
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return self.list[index.row()]
        return QVariant()

class ExpansionPicker(QDialog, Ui_ExpansionPicker):
    def __init__(self, delegate, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.delegate = delegate
        
        self.allExpModel = ExpansionPickerModel(self)
        for exp in utilities.allExpansions:
            try:
                self.allExpModel.addItem(utilities.expansionDict[exp])
            except KeyError:
                self.allExpModel.addItem(exp)
        self.lvAvailable.setModel(self.allExpModel)
        
        self.selectedModel = ExpansionPickerModel(self)
        self.lvSelected.setModel(self.selectedModel)
        
        self.connect(self.btnAdd, SIGNAL('clicked()'), self.addToSelected)
        self.connect(self.btnRemove, SIGNAL('clicked()'), self.removeFromSelected)
        self.connect(self.btnOK, SIGNAL('clicked()'), self.ok)
    def addToSelected(self):
        for index in self.lvAvailable.selectedIndexes():
            #self.selectedModel.addItem(self.allExpModel.list[index.row()])
            self.selectedModel.addItem(self.allExpModel.list[index.row()])
    def removeFromSelected(self):
        for index in self.lvSelected.selectedIndexes():
            self.selectedModel.removeItem(self.selectedModel.list[index.row()])
    
    def ok(self):
        self.delegate.setExpansions([utilities.allExpansions[self.allExpModel.list.index(exp)] for exp in self.selectedModel.list])
        self.accept()
def main():
    app = QApplication(sys.argv)
    d = ExpansionPicker(None)
    d.show()
    app.exec_()

if __name__ == '__main__':
    main()