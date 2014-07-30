'''
Created on Jul 19, 2011

@author: mitchell
'''

from UI.UI_deckEditor import Ui_DeckEditor
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, QString
from QItemPicker import QItemPicker
from Models.QDeckListModel import QDeckListModel
from statedb import Database, CardLookupException
import os

class QDeckEditor(QDialog, Ui_DeckEditor):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.openFile = None
        self.setupUi(self)
        
        openAction = QAction("",self)
        openAction.setShortcut(QKeySequence.Open)
        self.addAction(openAction)
        self.connect(openAction,SIGNAL("triggered()"),self.selectDeck)
        
        saveAction = QAction("",self)
        saveAction.setShortcut(QKeySequence.Save)
        self.addAction(saveAction)
        self.connect(saveAction,SIGNAL("triggered()"),self.saveDeck)
        
        self.connect(self.btnOpen, SIGNAL('clicked()'), self.selectDeck)
        self.connect(self.btnSave, SIGNAL('clicked()'), self.saveDeck)
        self.connect(self.btnNew,  SIGNAL('clicked()'), self.newDeck)

    def selectDeck(self):
        deckPicker = QItemPicker(self, self.deckPicked, QDeckListModel(self))
        deckPicker.show()

    def deckPicked(self, deck):
        self.openFile = deck
        self.setWindowTitle(deck)
        f = open(os.path.join('src','userdata','decks',deck))
        line = f.readline()
        if line.startswith("timeStamp:"):
            line = f.readline()

        deck = ""
        while line != "":
            deck += line
            line = f.readline()
        f.close()

        self.pteDeckEditor.setPlainText(deck)

    def saveDeck(self):
        if self.openFile is None:
            return
        deck = self.pteDeckEditor.toPlainText()
        f = open(os.path.join('src','userdata','decks',self.openFile), 'w')
        f.write(deck)
        f.close()

    def newDeck(self):
        deck, ok = QInputDialog.getText(self, "New Deck", "Enter deck name:")
        if ok:
            self.openFile = str(deck)
            self.setWindowTitle(deck)
        
if __name__ is '__main__':
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    d = QDeckEditor()
    d.show()
    d.raise_()
    app.exec_()
