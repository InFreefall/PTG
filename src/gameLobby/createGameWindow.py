#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from UI_createGameWindow import Ui_NewGameDialog
from Models.QStringListModel import QStringListModel
from Draft.expansionPicker import ExpansionPicker
from util import utilities

class ExpansionList(QStringListModel):
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if index.row() >= len(self.list):
            return QVariant()
        if role == Qt.DisplayRole:
            return utilities.expansionDict[self.list[index.row()]]
        return QVariant()

class CreateGameWindow(QDialog, Ui_NewGameDialog):
    def __init__(self, parentWindow):
        QDialog.__init__(self, parentWindow)
        self.setupUi(self)
        self.connect(self.cbGameType, SIGNAL('currentIndexChanged(int)'), self.currentIndexChanged)
        self.connect(self.btnSelectExpansions, SIGNAL('clicked()'), self.selectExpansions)
        self.currentIndexChanged(0)
        self.expansionsModel = ExpansionList()
        self.expansionsModel.list = ['m14','m14','m14']
        self.lvExpansions.setModel(self.expansionsModel)
    
    def setUsername(self, username):
        self.gameName.setText("%s's Game" % (username))
    
    def currentIndexChanged(self, newIndex):
        self.type = self.cbGameType.itemText(newIndex)
        def hideDraft():
            self.lvExpansions.hide()
            self.btnSelectExpansions.hide()
            self.lblChosenExpansions.hide()
        if self.type == "Draft":
            self.lvExpansions.show()
            self.btnSelectExpansions.show()
            self.lblChosenExpansions.show()
        else:
            hideDraft()
        
    
    def selectExpansions(self):
        ep = ExpansionPicker(self, self)
        ep.show()
    
    def setExpansions(self, expansions):
        self.expansionsModel.list = expansions
        print "CGW's exps are: %s" % (expansions)
        self.expansionsModel.reset()
