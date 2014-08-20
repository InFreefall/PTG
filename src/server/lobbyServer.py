import hashlib
import json
import logging
import os
import pdb
import sys
from PlayerBasedServer import PlayerBasedServer
sys.path.append('../gen-py')

from ThriftGameLobby import TGameLobby
from ThriftGameLobby.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

LOG_FILENAME = 'LobbyServer.log'

DIST_PATH = os.path.join('..','..','dist','PTG')

class Draft:
    def __init__(self):
        self.players = []
    def playerToRightOf(self, playerID):
        index = -1
        for i,player in enumerate(self.players):
            if player.playerID is playerID:
                index = i
                break
        index += 1
        if index == len(self.players):
            index = 0
        return self.players[index].playerID

class LobbyHandler(PlayerBasedServer):
    from ThriftGameLobby import TGameLobby as service
    def __init__(self):
        PlayerBasedServer.__init__(self, GLPlayer, GLEvent)
        self.games = {}
        self.greatestGameID = -1
        logging.basicConfig(level=logging.DEBUG)
        self.drafts = {}
        self.getFileChecksums()
    
    def GLregisterPlayer(self, playerName):
        playerID = self.registerPlayer(playerName)
        self.players[playerID].team = 0
        return playerID

    def GLunregisterPlayer(self, playerID):
        self.unregisterPlayer(playerID)
    
    def GLgetPlayersInLobby(self):
        return self.getPlayers()
    
    def GLnewGame(self, playerID, gameName, gameType, expansions):
        gameID = self.nextGameID()
        logging.info("Player %s started game %s" % (playerID, gameName))
        
        game = GLGame()
        game.gameID = gameID
        game.name = gameName
        game.owner = playerID
        game.type = gameType
        game.expansions = expansions
        game.players = []
        self.games[gameID] = game
        
        e = GLEvent()
        e.type = "addGame"
        e.data = [str(game.gameID)]
        e.sender = playerID
        self.addEvent(e)
        return game
    
    def GLcancelGame(self, playerID, game):
        e = GLEvent()
        e.type = "playerLeftGame"
        e.data = [str(game.gameID)]
        e.sender = playerID
        self.addEvent(e)
        logging.info("Player %s left game %s." % (playerID, game.gameID))
        
        if playerID is game.owner:
            e = GLEvent()
            e.type = "removeGame"
            e.data = [str(game.gameID)]
            e.sender = playerID
            self.addEvent(e)
            logging.info("Game %s was canceled." % (game.gameID))
            # del self.games[game.gameID]
    
    def GLgetGames(self):
        return self.games.values()
    
    def GLgetGame(self, gameID):
        try:
            return self.games[gameID]
        except:
            print "Error - could not get game with id %s" % gameID
    
    def GLgameWithID(self, gameID):
        return self.games[gameID]
    
    def GLrequestToJoinGame(self, playerID, gameID):
        game = self.games[gameID]
        player = self.players[playerID]
        game.players.append(player)
        player.currentGameID = gameID
        
        e = GLEvent()
        e.type = "playerJoinedGame"
        e.data = [str(game.gameID)]
        e.sender = playerID
        self.addEvent(e)
        
        logging.info("Player %s joined game %s" % (playerID, gameID))
        
        return True
    
    def GLswitchToTeam(self, playerID, gameID, team):
        game = self.games[gameID]
        player = self.players[playerID]
        player.team = team
        
        e = GLEvent()
        e.type = "playerSwitchedTeams"
        e.data = [str(gameID),str(team)]
        e.sender = playerID
        self.addEvent(e)
        
        logging.info("Player %s joined team %s" % (playerID, team))
    
    def GLstartGame(self, gameID):
        print "Game %d is starting" % (gameID)
        e = GLEvent()
        e.type = "gameStarted"
        e.data = [str(gameID)]
        e.sender = self.games[gameID].owner
        self.addEvent(e)
        if (self.games[gameID].type == "Draft"):
            d = Draft()
            self.drafts[gameID] = d
            d.players = self.games[gameID].players
    
    def GLcurrentEventIndex(self):
        return len(self.events)-1
    
    def GLgetEvents(self, sinceIndex):
        retVal = self.events[(sinceIndex+1):]
        return retVal
    
    def nextGameID(self):
        self.greatestGameID += 1
        return self.greatestGameID
    
    def addEvent(self, event):
        try:
            event.senderName = self.players[event.sender].playerName
        except:
            pass
        self.events.append(event)
        event.index = self.events.index(event)
    
    def GLpassExpansion(self, gameID, playerID, expansion):
        draft = self.drafts[gameID]
        e = GLEvent()
        e.type = "expansionPassedTo"
        e.data = [expansion, str(draft.playerToRightOf(playerID)), str(gameID)]
        e.sender = playerID
        self.addEvent(e)

    def hashfile(self, afile, hasher, blocksize=65536):
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        return hasher.hexdigest()
        
    def getFileChecksums(self):
        result = []
        with open(os.path.join(DIST_PATH, "files.lst")) as fList:
            for fname in fList:
                fname = fname.strip()
                fpath = os.path.join(DIST_PATH, fname)
                if not os.path.isfile(fpath):
                    print "Error: could not open file {} from files.lst".format(fpath)
                    continue
                with open(fpath) as currentFile:
                    fhash = self.hashfile(currentFile, hashlib.sha256())
                    result.append( {'filename': fname,
                                    'hash': fhash} )
        outputJson = json.dumps(result)
        with open(os.path.join(DIST_PATH, "files.json"), 'w') as outFile:
            outFile.write(outputJson)
        return outputJson

if __name__ == "__main__":
    server = LobbyHandler()
    server.run(TGameLobby, 42141, "Starting lobby...")
