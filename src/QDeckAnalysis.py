'''
Created on Aug 16, 2011

@author: mitchell
'''

from UI.UI_deckValidator import Ui_DeckValidatorDialog
from PyQt4.QtGui import QDialog, QStandardItemModel, QStandardItem, QBrush, QColor, QAction,QKeySequence
from PyQt4.QtCore import SIGNAL, QString
from QItemPicker import QItemPicker
from Models.QDeckListModel import QDeckListModel
from statedb import Database, CardLookupException
import os

canBeRepeated = ('Swamp','Island','Plains','Mountain','Forest','Relentless Rats')

class QDeckAnalysis(QDialog, Ui_DeckValidatorDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        openAction = QAction("",self)
        openAction.setShortcut(QKeySequence.Open)
        self.addAction(openAction)
        self.connect(openAction,SIGNAL("triggered()"),self.selectDeck)
        self.bgManaCurve.setValues([50,3,8,5,6])
        self.setupModel()
        self.db = Database()
        
        self.lblCurrentDeck.setText("Pick a deck")
        
        self.connect(self.btnSelectDeck, SIGNAL('clicked()'), self.selectDeck)
    
    def selectDeck(self):
        deckPicker = QItemPicker(self, self.deckPicked, QDeckListModel(self))
        deckPicker.show()
        
    def deckPicked(self, deck):
        self.lblCurrentDeck.setText(deck)
        
        commander = None
        
        errors = []
        cards = {}
        file = open(os.path.join('src','userdata','decks',deck))
        line = file.readline()
        if line.startswith("timeStamp:"):
            line = file.readline()
        while line != "":
            if line.strip() == '' or line.strip()[0] == '#':
                line = file.readline()
                continue
            if line.strip().startswith("Commander:"):
                commander = line.strip()[len("Commander:"):].strip()
                line = file.readline()
                continue
            parts = line.split(' x ')
            cardName = line.rstrip()
            numCards = 1
            if len(parts) is not 1:
                cardName = parts[1].rstrip()
                numCards = parts[0].rstrip()
            
            parts = cardName.split('/')
            if len(parts) is not 1 and parts[0] == "cards":
                cardName = self.db.nameForAbbreviationIndex(parts[1], parts[2]) # Card is referenced by /cards/abbreviation/index format
            
            # Check for unknown cards
            try:
                self.db.findCard(cardName)
            except CardLookupException:
                try:
                    errors.index(cardName)
                except ValueError:
                    errors.append(cardName)
            
            try:
                prevNum = cards[cardName]
            except KeyError:
                prevNum = 0
            cards[cardName] = int(numCards) + prevNum
            line = file.readline()
        
        # Display Errors
        # First reset previous errors
        self.missingCardsItem.removeRows(0,self.missingCardsItem.rowCount())
        self.missingCardsItem.setText("%s Unknown Cards:" % (len(errors)))
        if len(errors) == 0:
            self.setItemGreen(self.missingCardsItem)
        else:
            self.setItemRed(self.missingCardsItem)
        for error in errors:
            self.missingCardsItem.appendRow(QStandardItem(error))
        
        # Look for cards over 4 and count deck
        deckCount = 0
        self.repeatedCardsItem.removeRows(0,self.repeatedCardsItem.rowCount())
        for card in cards:
            if cards[card] > 4 and card not in canBeRepeated:
                self.repeatedCardsItem.appendRow(QStandardItem(card))
            deckCount += cards[card]
        rciCount = self.repeatedCardsItem.rowCount()
        self.repeatedCardsItem.setText("%s cards repeated over 4 times" % (rciCount))
        if rciCount is 0:
            self.setItemGreen(self.repeatedCardsItem)
        else:
            self.setItemRed(self.repeatedCardsItem)
        self.deckSizeItem.setText("%s cards in deck" % (deckCount))
        
        if commander is None:
            self.commanderItem.setText("No Commander")
            self.setItemRed(self.commanderItem)
        else:
            self.commanderItem.setText("Commander is %s" % (commander))
            self.setItemGreen(self.commanderItem)
        
        # Check if it is valid for standard play
        
        if deckCount >= 60 and rciCount == 0:
            # TODO: Check for illegal cards
            self.validForStandard.setText("Valid for standard play")
            self.setItemGreen(self.validForStandard)
        else:
            self.validForStandard.setText("Not valid for standard play")
            self.setItemRed(self.validForStandard)
        
        # Check if it is valid for commander
        
        if deckCount == 100 and commander is not None:
            self.validForCommander.setText("Valid for commander play")
            self.setItemGreen(self.validForCommander)
        else:
            self.validForCommander.setText("Not valid for commander play")
            self.setItemRed(self.validForCommander)
        
        # Analyze mana count
        
        
        cmcCounts = {"X" : 0}
        greatestCost = 0
        for card in cards:
            try:
                cmc = self.getCMC(self.db.manaCostForCard(card))
            except CardLookupException:
                continue
            if cmc == -1:
                continue # Must be a land or something
            if not cmc == "X" and  cmc > greatestCost:
                greatestCost = cmc
            try:
                cmcCounts[cmc] += cards[card]
            except KeyError:
                cmcCounts[cmc] = cards[card]
        
        values = []
        for cost in range(greatestCost+1):
            try:
                numCards = cmcCounts[cost]
            except KeyError:
                numCards = 0
            values.append(numCards)
        values.append(cmcCounts["X"])
        
        self.bgManaCurve.setValues(values)
            
    
    def getCMC(self, manaCost):
        if manaCost == "":
            return -1
        integer = "0"
        cmc = 0
        for char in manaCost:
            try:
                int(char)
                # If it gets to here, char is a number
                integer += char
            except ValueError:
                if char == "X":
                    return "X"
                if char in ("B", "R", "U", "G", "W"):
                    cmc += 1
        cmc += int(integer)
        return cmc
    
    def setupModel(self):
        self.tvIssues.setModel(QStandardItemModel(self))
        root = self.tvIssues.model().invisibleRootItem()
        
        self.missingCardsItem = QStandardItem("10 Unknown Cards:")
        self.deckSizeItem = QStandardItem("0 Cards in Deck")
        self.repeatedCardsItem = QStandardItem("3 Cards repeated over 4 times")
        self.commanderItem = QStandardItem("No commander")
        self.validForStandard = QStandardItem("Valid for standard play")
        self.validForCommander = QStandardItem("Not valid for commander play")
        
        
        root.appendRow(self.missingCardsItem)
        root.appendRow(self.deckSizeItem)
        root.appendRow(self.repeatedCardsItem)
        root.appendRow(self.commanderItem)
        root.appendRow(self.validForStandard)
        root.appendRow(self.validForCommander)
        for i in range(10):
            self.missingCardsItem.appendRow(QStandardItem(QString("Card %s" % (i))))
    
    def setItemRed(self, item):
        item.setForeground(QBrush(QColor(255,0,0)))
    def setItemGreen(self, item):
        item.setForeground(QBrush(QColor(0,180,0)))

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    d = QDeckAnalysis()
    d.show()
    d.raise_()
    app.exec_()
