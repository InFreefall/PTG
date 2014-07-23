import clickHandler
import crashReporter
import easygui
import notificationCenter
import pdb
import pygame
import sys
import os
from button import Button
from card import Card, MinimalCard
from cardScroller import CardScroller
from Networking import gameClient as client
from Networking.gameClient import Client
from Displayable import Displayable
from handPullDown import HandPullDown
from lifeCounter import LifeCounter
from player import Player
from pygame.locals import *
from reveal import Reveal
from util import utilities

class Battle(Displayable):
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,1024))
        self.fullscreen = False
        pygame.display.set_caption('Plamann: The Gathering')
        
        self.background = utilities.load_image(os.path.join('images','background.png'))[0]
        self.background = self.background.convert()
        
        try:
            os.mkdir('userdata')
        except:
            pass
        
        self.client = Client(self)
        client.sharedClient = self.client
        try:
            username = sys.argv[2]
        except:
            username = easygui.enterbox(msg="Enter Username:", title="Enter Username")
        if username is None:
            sys.exit(0)
        crashReporter.username = username
        self.client.addToBattle(username)

        notificationCenter.addObserver(self, self.changePlaceholder, "changePlaceholder")
        notificationCenter.addObserver(self, self.setContextMenu, utilities.setContextMenu)
        
        self.contextMenu = None

        self.player = Player(self, self.client, False)
        self.players = []
        self.currentOpponent = None
        
        battleUIGroup = "battleUI"
        
        self.leftArrow = Button(os.path.join('images', 'leftArrow.png'), self, battleUIGroup, size=(30,30))
        self.leftArrow.rect.topleft = (5,100)
        self.rightArrow = Button(os.path.join('images', 'rightArrow.png'), self, battleUIGroup, size=(30,30))
        self.rightArrow.rect.topleft = (925,100)
        self.buttons = [self.leftArrow, self.rightArrow]

        self.placeholder = Card('back',0,big=True);
        self.placeholder.rect.topleft = (964,6)
        
        self.lifeCounter = LifeCounter(self, self.client, battleUIGroup)
        self.lifeCounter.rect.topleft = (1068,461)
        
        self.untapAllButton = Button(os.path.join('images', 'untapAll.png'), self, battleUIGroup)
        self.untapAllButton.rect.topleft = (1060, 900)
        
        self.addTokenButton = Button(os.path.join('images', 'addToken.png'), self, battleUIGroup)
        self.addTokenButton.rect.topleft = (1060, 850)

        self.hand = HandPullDown(self, battleUIGroup)
        self.visor = None # Placeholder for a HandPullDown to show
        
        self.handyServer = None
        try:
            useBonjour = os.environ['PTGUSEBONJOUR'] == "YES"
        except:
            useBonjour = False
        if useBonjour:
            print "Trying to start bonjour and handy"
            from HandyServer import HandyServer
            self.handyServer = HandyServer(username, self)
            self.handyServer.start()

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            clock.tick(60)
            self.client.update()
            events = pygame.event.get()
            for event in events:
                if event.type is QUIT:
                    print "Thank you for playing! Closing now..."
                    self.client.disconnect()
                    sys.exit()
                elif event.type is MOUSEMOTION:
                    clickHandler.move(event.pos)
                elif event.type is MOUSEBUTTONDOWN:
                    clickHandler.click(event.pos, event.button)
                elif event.type is MOUSEBUTTONUP:
                    clickHandler.endClick(event.pos, event.button)
                elif event.type is KEYDOWN:
                    if event.key is K_f:
                        if self.fullscreen:
                            self.screen = pygame.display.set_mode((1280,1024))
                        else:
                            self.screen = pygame.display.set_mode((1280,1024), FULLSCREEN)
                        self.fullscreen = not self.fullscreen
                if self.currentOpponent is not None:
                    self.currentOpponent.update(event)
                self.player.update(event)
                self.hand.update(event)
                if self.visor is not None:
                    self.visor.update(event)
            self.draw(events)

    def draw(self, events):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.untapAllButton.image, self.untapAllButton.rect.topleft)
        self.screen.blit(self.addTokenButton.image, self.addTokenButton.rect.topleft)
        self.screen.blit(self.placeholder.image, self.placeholder.rect)
        self.screen.blit(self.lifeCounter.image, self.lifeCounter.rect)
        if self.currentOpponent is not None:
            self.currentOpponent.draw(self.screen)
        [self.screen.blit(button.image, button.rect.topleft) for button in self.buttons]
        self.hand.draw(self.screen)
        if self.visor is not None:
            self.visor.draw(self.screen)
        self.player.draw(self.screen)
        if self.contextMenu is not None:
            self.contextMenu.draw(self.screen)
        pygame.display.flip()

    def changePlaceholder(self, minimalCard):
        self.placeholder.setImage(minimalCard.abbreviation, minimalCard.index, True)

    def setContextMenu(self, contextMenu):
        self.contextMenu = contextMenu

    def registerPlayer(self, playerID, playerName):
        player = Player(self, self.client, isOpponent=True, playerID=playerID)
        player.setName(playerName)
        self.players.append(player)
        self.setCurrentOpponent(player)
        print playerName+ " joined with ID: " + str(playerID)
    
    def unregisterPlayer(self, playerID):
        leavingPlayer = None
        for player in self.players:
            if player.playerID == playerID:
                leavingPlayer = player
        if leavingPlayer is None:
            print "Error occurred. List of players:"
            print self.players
            raise Exception("Something happened: A player left that I didn't know existed.  playerID was %d.  My apologies" % (playerID))
        self.players.remove(leavingPlayer)
        if self.currentOpponent is leavingPlayer:
            if len(self.players) > 0:
                self.setCurrentOpponent(self.players[0])
            else:
                self.setCurrentOpponent(None)
    
    def setDeck(self, playerID, deckName, deckSize):
        print "Setting deck: (%s, %s, %s)" % (playerID, deckName, deckSize)
        player = None
        for p in self.players:
            if p.playerID == playerID:
                player = p
        if player is None:
            print "Error occurred. List of players:"
            print self.players
            raise Exception("Something happened: A player left that I didn't know existed.  playerID was %d.  My apologies" % (playerID))
        player.deckSize = deckSize
        player.deckName = deckName
        player.setDeckSize()
    
    def moveCard(self, playerID, abbreviation, index, originalPosition, newPosition, tapped):
        curPlayer = None
        card = None
        for player in self.players:
            if player.playerID == playerID:
                curPlayer = player
        if curPlayer is None:
            raise Exception("A player did something, but I don't know who that player is!")
        if not self.hand.hidden and not newPosition == client.HAND and not originalPosition == client.DECK:
            self.hand.toggleHidden()
        if originalPosition == client.HAND or originalPosition == client.DECK or originalPosition == client.GRAVEYARD or originalPosition == client.TOKEN:
            card = Card(abbreviation, index, curPlayer, big=False)
            if originalPosition == client.DECK:
                curPlayer.deckSize -= 1
                curPlayer.setDeckSize()
        curPlayer.moveCard(originalPosition, newPosition, tapped, card)
        self.setCurrentOpponent(curPlayer)
    
    def setPlayerLife(self, playerID, life):
        curPlayer = None
        for player in self.players:
            if player.playerID == playerID:
                curPlayer = player
        if curPlayer is None:
            raise Exception("A player did something, but I don't know who that player is!")
        curPlayer.setLife(life)
    
    def revealCard(self, abbreviation, index, playerName):
        Reveal(Card(abbreviation,index,big=True), playerName, self)
    
    def refreshHand(self):
        # Synchronize the handPullDown's display with the players
        self.hand.scroller.setCards(self.player.hand)
        #self.hand.scroller.scrollBar.scroll(self.hand.scroller.rect.width)
    
    def showHand(self):
        if self.hand.hidden:
            self.hand.toggleHidden()
    
    def absoluteRect(self):
        return pygame.Rect((0,0), (1280,1024))

    def buttonClicked(self, position, sender, mouseButton):
        if mouseButton is not 1:
            return
        if sender is self.leftArrow or sender is self.rightArrow:
            if not self.hand.hidden:
                return False
            if self.currentOpponent is None:
                return False
            opponentIndex = self.players.index(self.currentOpponent)
            if sender is self.leftArrow:
                opponentIndex -= 1
                if opponentIndex < 0:
                    opponentIndex = len(self.players) - 1
            elif sender is self.rightArrow:
                opponentIndex += 1
                if opponentIndex >= len(self.players):
                    opponentIndex = 0
            self.setCurrentOpponent(self.players[opponentIndex])
        elif sender is self.untapAllButton:
            self.player.untapAll()
        elif sender is self.addTokenButton:
            if self.fullscreen:
                self.fullscreen = False
                self.screen = pygame.display.set_mode((1280,1024))
            dirList = os.listdir(os.path.join('images',"tokens"))
            dirList = [os.path.splitext(file)[0] for file in dirList if not file.startswith('.')]
            token = easygui.choicebox("NO FULLSCREEN FOR U!", "Pick a token:", dirList)
            if (token == None):
                return
            card = Card('tokens', token, self.player)
            self.player.creatureScroller.addCard(card)
            self.client.moveCard(card.abbreviation, card.index, client.TOKEN, card.position, card.tapped)
            
    def setCurrentOpponent(self, newCurOpponent):
        if self.currentOpponent is not None:
            clickHandler.setClickable(self.currentOpponent.group, False)
        self.currentOpponent = newCurOpponent
        if self.currentOpponent is not None:
            clickHandler.setClickable(self.currentOpponent.group, True)
    
    def setVisor(self, visor):
        if not self.hand.hidden:
            self.hand.toggleHidden()
        self.visor = visor