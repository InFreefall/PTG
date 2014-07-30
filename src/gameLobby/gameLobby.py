#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# Needs to be first - settingsManager tries to use this directory on import
import os
userdataPath = os.path.join('src','userdata','decks')
try:
    print "Trying to create userdata directory"
    os.makedirs(userdataPath)
except OSError:
    pass # Directory already exists


import sys
from QDeckAnalysis import QDeckAnalysis
from QDeckEditor import QDeckEditor
from QVisualDeckEditor import QVisualDeckEditor
sys.path.append('../gen-py')

from Networking import GLclient

# Dialogs
from createGameWindow import CreateGameWindow
from inGameDialog import InGameDialog
from QSettingsDialog import QSettingsDialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_gameLobby import Ui_MainWindow

from PTG import PTG
import QPTG
from PTG.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from util import utilities
import settingsManager
import crashReporter

class GameLobby(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GameLobby, self).__init__()
        self.setupUi(self)

        self.setupMenus()

        self.connect(self.btnCreateGame, SIGNAL('clicked()'), self.displayWindow)
        self.connect(self.btnJoinGame, SIGNAL('clicked()'), self.joinGameButtonClicked)

        self.client = GLclient.Client(self)

        self.show()
        self.raise_()  # Make sure my window is on top
        text = QInputDialog.getText(self, 'Enter Username', 'Please enter your username:')[0]
        if not text == "":
            self.username = text
        else:
            self.username = "Anonymous"
        crashReporter.username = self.username
        self.client.register(self.username)

        self.lvGames.setModel(self.client.gameModel)
        self.lvPlayers.setModel(self.client.playerModel)

    def setupMenus(self):
        bar = self.menuBar()
        tools = bar.addMenu("&Tools")
        tools.addAction("Deck Analyzer", self.showAnalysis)
        tools.addAction("Deck Editor", self.showEditor)
        tools.addAction("Visual Deck Editor", self.showVisualEditor)
        tools.addAction("Preferences",self.showSettings)

    def showSettings(self):
        dialog = QSettingsDialog(self)
        dialog.show()

    def showAnalysis(self):
        dialog = QDeckAnalysis(self)
        dialog.show()

    def showEditor(self):
        dialog = QDeckEditor(self)
        dialog.show()

    def showVisualEditor(self):
        dialog = QVisualDeckEditor(self)
        dialog.show()

    def displayWindow(self):
        self.cgw = CreateGameWindow(self)
        self.cgw.setUsername(self.username)
        self.connect(self.cgw, SIGNAL('accepted()'), self.addNewGame)
        self.connect(self.cgw, SIGNAL('rejected()'), self.cancelNewGame)
        self.cgw.show()

    def addNewGame(self):
        gameName = self.cgw.gameName.text()
        gameType = self.cgw.type
        game = self.client.createGame(gameName, gameType, self.cgw.expansionsModel.list)
        self.cgw = None
        self.joinGame(game)

    def joinGameButtonClicked(self):
        selectedIndex = self.lvGames.selectedIndexes()[0]
        row = selectedIndex.row()
        game = self.client.gameModel.list[row]
        if not game.started:
            self.joinGame(game)
        else:
            self.joinInProgressGame(game)

    def joinGame(self, game):
        self.client.joinGame(game)
        igd = InGameDialog(self.client, self)
        igd.setGame(game)
        self.connect(igd, SIGNAL('finished(int)'), self, SLOT('show()'))
        self.hide()
        igd.show()

    def joinInProgressGame(self, game):
        if game.type in ("Constructed", "Two-Headed Giant", "Commander", "Yu-Gi-Oh", "Random Decks"):
            team = -1
            gameType = -1
            if game.type == "Two-Headed Giant":
                team = -1 # TODO: Get team # back
                gameType = utilities.kGameTypeTwoHeadedGiant
            elif game.type == "Commander":
                gameType = utilities.kGameTypeCommander
            elif game.type == "Yu-Gi-Oh":
                gameType = utilities.kGameTypeYuGiOh
            elif game.type == "Random Decks":
                gameType = utilities.kGameTypeRandomDecks
            else:
                gameType = utilities.kGameTypeStandard
            dialog = QPTG.GameDialog(game.gameID, gameType, self, fastForward=True)
            dialog.team = team
            dialog.setUsername(self.client.username)
            dialog.show()

    def cancelNewGame(self):
        self.cgw = None

    def connectToServer(self, hostname):
        settingsManager.settings['hostname'] = hostname
        self.client = GLclient.Client(self)

        if self.client.VERSION() != utilities.VERSION():
            # Version mismatch - cannot connect to this server
            pass

        self.client.register(self.username)

def maintenance():
    pass

def testConnection():
    ableToRun = True
    versionMismatch = False
    try:
        transport = TSocket.TSocket(settingsManager.settings['hostname'], 42142)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = PTG.Client(protocol)
        transport.open()
        print "Server version: ", client.VERSION()
        print "My version: ", utilities.VERSION(), "\n"
        if client.VERSION() != utilities.VERSION():
            ableToRun = False
            versionMismatch = True
            print "Houston, we have a problem. Version mismatch."
            QMessageBox.critical(None,"Critical Error!","Version mismatch -- please update client.")
    except Exception, ex:
        print ex
        ableToRun = False
    finally:
        transport.close()
    return (ableToRun, versionMismatch)

def main():
    # In development, this causes more trouble than it's worth
    # crashReporter.install_excepthook()
    maintenance()
    app = QApplication(sys.argv)
    ableToRun,versionMismatch = testConnection()
    if versionMismatch:
        sys.exit(1) # Can't continue with a version mismatch
    shouldTryAgain = True
    while not ableToRun and shouldTryAgain and not versionMismatch:
        # Present message box asking for alternative server
        server = QInputDialog.getText(None, "Could not connect to server!", "Enter an alternate server:", text=settingsManager.settings['hostname'])
        if server[1]:
            settingsManager.settings['hostname'] = str(server[0])
        else:
            shouldTryAgain = False
            break
        ableToRun,versionMismatch = testConnection()
    iconPath = os.path.join(settingsManager.settings['imagesDir'],"icon.png")
    app.setWindowIcon(QIcon(iconPath))
    result = 1
    if ableToRun:
        settingsManager.save()
        lobbyWindow = GameLobby()
        result = app.exec_()
        lobbyWindow.client.disconnect()
    sys.exit(result)

if __name__ == '__main__':
    main()
