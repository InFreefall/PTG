'''
Created on Jul 13, 2011

@author: mitchell
'''

from PyQt4.QtGui import QWidget
from UI.UI_opponentInfo import Ui_OpponentInfo

class QPlayerInfo(QWidget, Ui_OpponentInfo):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self._life = 20
        self._poison = 0
        self._handSize = 0
        self._deckSize = 0
    
    def setLife(self, life):
        self.lblLife.setText(str(life))
        self._life = life
    def life(self):
        return self._life
    def setPoison(self, poison):
        self.lblPoison.setText(str(poison))
        self._poison = poison
    def poison(self):
        return self._poison
    def setHandSize(self, handSize):
        self.lblHandSize.setText(str(handSize))
        self._handSize = handSize
    def handSize(self):
        return self._handSize
    def setDeckSize(self, deckSize):
        self.lblDeckSize.setText(str(deckSize))
        self._deckSize = deckSize
    def deckSize(self):
        return self._deckSize

    def hidePoison(self):
        self.lblPoison.hide()
        self.lblPoisonLabel.hide()
