'''
Created on Jul 10, 2011

@author: mitchell
'''

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL
from UI.UI_deckPickerDialog import Ui_DeckPickerDialog

class QItemPicker(QDialog, Ui_DeckPickerDialog):
    def __init__(self, delegate, callback, model, itemName="Deck"):
        QDialog.__init__(self, delegate)
        self.callback = callback
        self.setupUi(self)
        self.lvDecks.setModel(model)
        self.connect(self, SIGNAL('accepted()'), self.deckSelected)
        self.btnChoose.setText("Choose This %s" % (itemName))
        self.setWindowTitle("Select a %s" % (itemName))
        self.activateWindow()
    
    def deckSelected(self):
        index = self.lvDecks.selectedIndexes()[0]
        deck = self.lvDecks.model().fileForRow(index.row())
        self.callback(deck)

    def closeEvent(self, argumentIgnored):
        self.callback(self.lvDecks.model().fileForRow(0)) # Pick random deck if x button is clicked
