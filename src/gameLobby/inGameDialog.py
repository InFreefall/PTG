#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os
import time
import subprocess
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_inGameDialog import Ui_InGameDialog
from Models.GLModels import GLPlayerList
from Draft.updatedDraftDialog import DraftDialog
import QPTG
import QPTGRules
from Networking.DraftClient import DraftClient
from util import utilities

class InGameDialog(QDialog, Ui_InGameDialog):
    def __init__(self, client, parentWindow):
        QDialog.__init__(self, parentWindow)
        self.deletesListener = True
        self.setupUi(self)
        self.client = client
        self.connect(self, SIGNAL('rejected()'), self.cancelGame)
        self.connect(self.btnStartGame, SIGNAL('clicked()'), self.startGameButtonClicked)
        self.connect(self.btnSwitchTeams, SIGNAL('clicked()'), self.switchTeam)
        self.playerList = GLPlayerList(self.client.playerID)
        self.lvPlayers.setModel(self.playerList)
        self.teams = [GLPlayerList(self.client.playerID),GLPlayerList(self.client.playerID)]
        self.lvTeam1.setModel(self.teams[0])
        self.lvTeam2.setModel(self.teams[1])
    
    def setGame(self, game):
        self.client.registerListenerForGame(self, game)
        self.game = self.client.gameWithIndex(game.gameID) # make sure game has most recent list of players
        [self.playerList.addItem(player) for player in self.game.players]
        [self.teams[player.team].addItem(player) for player in self.game.players]
        self.setWindowTitle(game.name)
        if self.client.playerID is not self.game.owner:
            self.btnStartGame.setEnabled(False)
        else:
            self.btnStartGame.setEnabled(True)
        
        if self.game.type == "Two-Headed Giant":
            self.lvPlayers.hide()
        else:
            self.wTwoHeadedGiant.hide()
    
    def cancelGame(self):
        '''Tells the server that the game is no longer running.'''
        self.client.cancelGame(self.game)
    
    def addPlayer(self, player):
        self.playerList.addItem(player)
        if player.team != -1:
            self.teams[player.team].addItem(player)
    
    def removePlayer(self, player):
        self.playerList.removeItem(player)
        if player.team != -1:
            self.teams[player.team].removeItem(player)
    
    def gameWasCanceled(self):
        self.disconnect(self, SIGNAL('rejected()'), self.cancelGame)
        self.reject()
    
    def startGameButtonClicked(self):
        # I clicked it, so I must be the game's owner
        self.client.startGame(self.game)
        self.startGame()
    
    def teamChangedForPlayer(self, player):
        for team in self.teams:
            try:
                team.removeItem(player)
            except ValueError:
                pass # Player was not on this team before
        self.teams[player.team].addItem(player)
    
    def switchTeam(self):
        me = self.playerList.playerForID(self.client.playerID)
        self.teams[me.team].removeItem(me)
        me.team = (me.team+1)%2
        self.teams[me.team].addItem(me)
        self.client.switchToTeam(self.game.gameID, me.team)
    
    def startGame(self):
        if self.game.type in ("Constructed", "Two-Headed Giant", "Commander", "Yu-Gi-Oh", "Random Decks"):
            self.reject()
            team = -1
            gameType = -1
            if self.game.type == "Two-Headed Giant":
                team = self.playerList.playerForID(self.client.playerID).team
                gameType = utilities.kGameTypeTwoHeadedGiant
            elif self.game.type == "Commander":
                gameType = utilities.kGameTypeCommander
            elif self.game.type == "Yu-Gi-Oh":
                gameType = utilities.kGameTypeYuGiOh
            elif self.game.type == "Random Decks":
                gameType = utilities.kGameTypeRandomDecks
            else:
                gameType = utilities.kGameTypeStandard
            dialog = QPTG.GameDialog(self.game.gameID, gameType, self.parent())
            dialog.team = team
            dialog.setUsername(self.client.username)
            dialog.show()
            dialog.pickDeck() # Start the game.
                              # PickDeck is here because then the deck picker shows up above the game dialog
        elif self.game.type == "Draft":
            print "Draft game started..."
            self.deletesListener = False
            client = DraftClient()
            client.setUp(self.game.gameID, len(self.game.players), self.game.expansions)
            client.register(self.client.username)
            dialog = DraftDialog(client, self.parent())
            dialog.show()
            self.reject()
