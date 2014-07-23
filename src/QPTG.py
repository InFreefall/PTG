#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys
from PyQt4.QtGui import QDialog, QPixmap, QApplication, QMenu, QIcon
from PyQt4.QtCore import SIGNAL, Qt
from UI.UI_MainPTG import Ui_MainPTG
import Networking.QGameClient
from QPlayer import QPlayer
from Models.QCardModel import QCardModel
from QItemPicker import QItemPicker
from QCMI import ClientModelInterface
from Models.QDeckListModel import QDeckListModel
from Models.QRandomDeckListModel import QRandomDeckListModel
import os
import settingsManager
from UI.QCardListViewer import QCardListViewer
from util import utilities
import statedb

class GameDialog(QDialog, Ui_MainPTG):
    def __init__(self, gameID, gameType, parent=None, fastForward=False):
        QDialog.__init__(self, parent)
        self.client = Networking.QGameClient.QGameClient(self, gameID, fastForward) # Used by setupUi
        self.players = {}
        self.team = 0
        self.soundFile = ''
        self.gameType = gameType
        
        self.setupUi(self)
    
    def setupUi(self, parent):
        Ui_MainPTG.setupUi(self, parent)
        self.setWindowFlags(Qt.Window)
        if self.gameType is utilities.kGameTypeYuGiOh:
            self.lblSelectedCard.setPixmap(QPixmap('images/yugiohBack.jpg').scaledToHeight(445))
            self.sbPoison.hide()
            self.lblPoison.hide()
            self.sbLife.setValue(8000)
        else:
            self.lblSelectedCard.setPixmap(QPixmap('images/back.jpg'))
        self.twTeam.clear()
        self.twOpponents.clear()
        
        self.handModel = QCardModel(self, True)
        self.lvHand.setModel(self.handModel)
        self.connect(self.handModel, SIGNAL('rowsInserted(QModelIndex,int,int)'), self.updateHandSize)
        self.connect(self.handModel, SIGNAL('rowsRemoved(QModelIndex,int,int)'), self.updateHandSize)
        ClientModelInterface(self.handModel, self.client, Networking.QGameClient.HAND)
        self.updateHandSize()

        self.connect(self.lvHand, SIGNAL('clicked(QModelIndex)'), self.enlargeCardFromHand)
        self.connect(self.sbLife, SIGNAL('valueChanged(int)'), self.client.setLife)
        self.connect(self.sbPoison, SIGNAL('valueChanged(int)'), self.client.setPoison)
        self.connect(self.btnViewExile, SIGNAL('clicked()'), self.viewExile)
        
    def setupPlayer(self):
        self.twTeam.addTab(self.pPlayer, QIcon(os.path.join('images','you.jpg')), self.client.username)
        self.connect(self.btnUntapAll, SIGNAL('clicked()'), self.pPlayer.untapAll)
        self.connect(self.btnAddToken, SIGNAL('clicked()'), self.pPlayer.askToAddToken)
        
        # Would be in setupUi, but needs player to function
        self.connect(self.lvHand, SIGNAL('customContextMenuRequested(QPoint)'), self.handModel.contextMenuFunction(self.lvHand, self.pPlayer, self, self))
        
        ClientModelInterface(self.pPlayer.creaturesModel, self.client, Networking.QGameClient.CREATURES)
        ClientModelInterface(self.pPlayer.landsModel, self.client, Networking.QGameClient.LANDS)
        ClientModelInterface(self.pPlayer.graveyardModel, self.client, Networking.QGameClient.GRAVEYARD)
        ClientModelInterface(self.pPlayer.deck, self.client, Networking.QGameClient.DECK)
        ClientModelInterface(self.pPlayer.exileModel, self.client, Networking.QGameClient.EXILE)
        
    def pickDeck(self):
        self.client.syncDecks()
        game = "Magic"
        if self.gameType == utilities.kGameTypeYuGiOh:
            game = "Yu-Gi-Oh"
        if self.gameType is not utilities.kGameTypeRandomDecks:
            deckPicker = QItemPicker(self, self.deckSelected, QDeckListModel(self,game))
            deckPicker.show()
        else:
            deckPicker = QItemPicker(self, self.randomDeckSelected, QRandomDeckListModel(self))
            deckPicker.show()
    
    def deckSelected(self, filename):
        print "Deck selected: %s" % (filename)
        self.pPlayer.setDeckFromFile(filename)
        self.client.setDeck(filename, len(self.pPlayer.deck.list))

    def randomDeckSelected(self, color):
        print "Random deck of color: %s" % (color)
        self.pPlayer.setRandomDeckFromColors(color)
        self.client.setDeck("Random: %s" % (color), len(self.pPlayer.deck.list))
    
    def setUsername(self, username):
        """Called to let the server know I am here and who I am."""
        self.client.addToBattle(username, self.team)
        self.pPlayer = QPlayer(self.handModel, gameDialog=self, gameType=self.gameType,
                               controllable=True, playerName=username, parent=self)
        self.setupPlayer()
    
    def closeEvent(self, event):
        self.client.disconnect()
        statedb.closeDB()
        event.accept()
    
    def enlargeCardFromHand(self, index):
        self.enlargeCard(self.handModel.list[index.row()])
        
    def enlargeCard(self, card, flipped=False):
        if not flipped:
            self.lblSelectedCard.setPixmap(card.pixmap())
        else:
            self.lblSelectedCard.setPixmap(card.bottomPixmap())
    
    def updateHandSize(self, ignoredIndex1=None, ignoredIndex2=None, ignored3=None):
        self.lblHand.setText("Your Hand (%d Cards):" % (len(self.handModel.list)))
    
    def displayHandMenu(self, pt):
        def flipCard():
            for index in self.lvHand.selectedIndexes():
                self.handModel.flipCardAtIndex(index)
        menu = QMenu(self)
        menu.addAction("Flip", flipCard)
        menu.exec_(self.lvHand.mapToGlobal(pt))
    
    def viewExile(self):
        QCardListViewer(self.pPlayer.exileModel, self.enlargeCard, self)

    ##############################################
    ####  Networking methods  ####################
    #### Called by the client ####################
    ##############################################
    
    def registerPlayer(self, playerID, playerName, team):
        print "Player %s joined with ID %s" % (playerName, playerID)
        player = QPlayer(self.handModel, gameDialog=self, gameType=self.gameType,
                         controllable=False, playerName=playerName, parent=self)
        player.hideDeck()
        if team == self.team and team is not -1:
            self.twTeam.addTab(player, playerName)
        else:
            self.twOpponents.addTab(player, playerName)
            player.flip()
        player.setGameType(self.gameType)
        self.players[playerID] = player
    
    def unregisterPlayer(self, playerID):
        player = self.players[playerID]
        try:
            self.twOpponents.removeTab(self.twOpponents.indexOf(player))
        except:
            self.twTeam.removeTab(self.twTeam.indexOf(player))
        del self.players[playerID]

    def setPlayerLife(self, playerID, life):
        player = self.players[playerID]
        player.piPlayerInfo.setLife(life)
        # Causes ugly echo effect -- not good
        # try:
        #     index = self.twTeam.indexOf(player)
        #     # If it gets to here, player is an ally
        #     if life is not self.sbLife.value():
        #         self.sbLife.setValue(life)
        # except:
        #     pass
    
    def setPlayerPoison(self, playerID, poison):
        self.players[playerID].piPlayerInfo.setPoison(poison)
    
    def setPlayerDeck(self, playerID, deckName, deckSize):
        self.players[playerID].piPlayerInfo.setDeckSize(deckSize)
    
    def addCardTo(self, playerID, pickledCard, zone, position):
        self.players[playerID].addCardTo(pickledCard, zone, position)
        if int(zone) in Networking.QGameClient.switchToZones:
            self.switchToPlayer(playerID)
    def removeCardFrom(self, playerID, zone, position):
        self.players[playerID].removeCardFrom(zone, position)
        if int(zone) in Networking.QGameClient.switchToZones:
            self.switchToPlayer(playerID)
    def setCardTo(self, playerID, pickledCard, zone, position):
        self.players[playerID].setCardTo(pickledCard, zone, position)
        if int(zone) in Networking.QGameClient.switchToZones:
            self.switchToPlayer(playerID)
    
    def switchToPlayer(self, playerID):
        if not settingsManager.settings['switchOnPlayerMove']:
            return
        player = self.players[playerID]
        index = self.twOpponents.indexOf(player)
        if index == -1:
            index = self.twTeam.indexOf(player)
        else:
            self.twOpponents.setCurrentIndex(index)
def main():
    app = QApplication(sys.argv)
    d = GameDialog(0)
    d.show()
    d.raise_()
    app.exec_()

if __name__ == '__main__':
    main()
