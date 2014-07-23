import clickHandler
from Networking import gameClient as client
import easygui
import inspect
import notificationCenter
import os
import pdb
import pygame
import random
from button import Button
from cardScroller import CardScroller
from card import Card, MinimalCard
from contextMenu import ContextMenu
from deck import Deck
from deckVisor import DeckVisor
from Displayable import Displayable
from graveyardVisor import GraveyardVisor
from handPullDown import HandPullDown
from util import utilities
import settingsManager

class Player(Displayable):
    def absoluteRect(self):
        if self.isOpponent:
            return self.surface.get_rect()
        else:
            return self.surface.get_rect().move(0,513)

    def __init__(self, battle, client, isOpponent = True, playerID = -1):
        self.battle = battle
        self.client = client
        self.isOpponent = isOpponent
        self.surface = pygame.surface.Surface((960,511))
        self.nameSurface = None
        if self.isOpponent:
            self.group = "Player%d" % (playerID)
        else:
            self.group = "localPlayer"
        self.graveyard = []
        self.life = 20
        self.name = ""
        self.landScroller = CardScroller(pygame.Rect(40,30,739,200), self, self.group, draggable = not isOpponent)
        self.creatureScroller = CardScroller(pygame.Rect(40,275,739,200), self, self.group, draggable = not isOpponent)
        self.creatureScroller.positionMod = 1
        self.handSize = 0
        if isOpponent:
            self.deckSize = 0
            self.deckName = ""
        else:
            self.hand = []
            self.deck = Deck()
            self.client.syncDecks()
            self.chooseDeck()
            self.deck.shuffle()
            self.client.setDeck(self.deck.name, len(self.deck.cards))
        
        if self.isOpponent and playerID is -1:
            raise Exception("An opponent must be assigned a playerID")
        self.playerID = playerID
        
        self.graveyardSprite = Button(os.path.join('images','empty.jpg'), self, self.group, size=(135,193))
        self.graveyardSprite.rect.topleft = (785,275)
        self.graveyardSprite.parent = self
        path = os.path.join('images','back.jpg')
        self.deckSprite = Button(path, self, self.group, size=(135,193))
        self.deckSprite.rect.topleft = (785,30)
        self.spriteGroup = pygame.sprite.RenderPlain((self.graveyardSprite,self.deckSprite))
        if not isOpponent:
            self.graveyardSprite.rect, self.deckSprite.rect = self.deckSprite.rect, self.graveyardSprite.rect
        self.setDeckSize()
        self.contextMenu = None
        
        self.draggingCard = None
        if not isOpponent:
            self.landScroller, self.creatureScroller = self.creatureScroller, self.landScroller
            self.draggingCard = None
        self.scrollers = [self.landScroller, self.creatureScroller] # This order is important to the moveCard function
        if self.isOpponent:
            [scroller.setTappable(False) for scroller in self.scrollers]

    def chooseDeck(self):
        dirList = os.listdir(os.path.join('src',"userdata",'decks'))
        dirList = [file for file in dirList if (not file.startswith('.')) and (file not in ('PTG.settings'))]
        readible = [os.path.splitext(file)[0] for file in dirList]
        readible.insert(0, " Random Deck")
        index = readible.index(easygui.choicebox("Choose a deck:", "Choose a deck", readible)) - 1
        if index is -1:
            deckName = random.choice(dirList)
        else:
            deckName = dirList[index]
        self.deck.loadFromFile(deckName)

    def setName(self, name):
        self.name = name
        self.nameSurface = pygame.font.Font(None,20).render("Opponent: %s   Life: %d    %d cards in hand" % (name, self.life, self.handSize), True, (255,255,255))
    
    def setLife(self, life):
        self.life = life
        self.setName(self.name)
    
    def setDeckSize(self):
        if self.isOpponent:
            number = self.deckSize
        else:
            number = len(self.deck.cards)
        self.deckLabel = pygame.font.Font(None,20).render("%d Cards" % (number), True, (255,255,255))

    def draw(self, surface):
        self.surface.fill((0,0,0))
        #self.surface.set_alpha(0)
        [scroller.draw(self.surface) for scroller in self.scrollers]
        self.spriteGroup.draw(self.surface)
        if self.draggingCard is not None:
            position = self.positionInSelf(self.draggingCard.draggingPosition)
            if position[0] < 0:
                position = (0, position[1])
            if position[0] > self.surface.get_width() - self.draggingCard.rect.width:
                position = (self.surface.get_width() - self.draggingCard.rect.width, position[1])
            if position[1] < 0:
                position = (position[0], 0)
            if position[1] > self.surface.get_height() - self.draggingCard.rect.height:
                position = (position[0], self.surface.get_height() - self.draggingCard.rect.height)
            #self.surface.blit(self.draggingCard.image, position)
        if self.nameSurface != None:
            self.surface.blit(self.nameSurface, (300,2))
        self.surface.blit(self.deckLabel, self.deckSprite.rect.move(0,10).bottomleft)
        if self.isOpponent:
            surface.blit(self.surface, (0,0))
        else:
            surface.blit(self.surface, (0, 513))
        
        if self.draggingCard is not None:
            surface.blit(self.draggingCard.image, self.draggingCard.draggingPosition)
        
        if self.contextMenu is not None:
            self.contextMenu.draw(surface)

    def update(self, event):
        [scroller.update(event) for scroller in self.scrollers]

    def endDragging(self, position):
        if self.draggingCard is None:
            return
        spriteTargets = [self.deckSprite,self.graveyardSprite]
        for scroller in self.scrollers:
            if scroller.absoluteRect().collidepoint(position) and (self.draggingCard.parent is not scroller):
                originalPosition = self.draggingCard.position
                self.draggingCard.parent.removeCard(self.draggingCard)
                if originalPosition is client.DECK:
                    self.deck.cards.remove(self.draggingCard.deckCard)
                    self.setDeckSize()
                elif originalPosition is client.GRAVEYARD:
                    self.removeCardFromGraveyard(self.draggingCard)
                    self.updateGraveyardImage()
                scroller.addCard(self.draggingCard)
                #newPosition = scroller.cards.index(self.draggingCard) * 2 + self.scrollers.index(scroller)
                self.client.moveCard(self.draggingCard.abbreviation, self.draggingCard.index, originalPosition, self.draggingCard.position, self.draggingCard.tapped)

        for sprite in spriteTargets:
            if sprite.absoluteRect().collidepoint(position):
                if sprite is self.deckSprite:
                    self.returnToDeck(self.draggingCard)
                elif sprite is self.graveyardSprite:
                    # Order matters here - sendToGraveyard changes self.draggingCard.position (oh, the pain)
                    self.client.moveCard(self.draggingCard.abbreviation, self.draggingCard.index, self.draggingCard.position, client.GRAVEYARD, False)
                    self.sendToGraveyard(self.draggingCard)
                    self.draggingCard.parent.removeCard(self.draggingCard)
        self.draggingCard = None

    def updateGraveyardImage(self):
        if len(self.graveyard) > 0:
            image, rect = utilities.load_image(os.path.join(settingsManager.settings['cardsDir'], self.graveyard[0].abbreviation, str(self.graveyard[0].index) + '.jpg'))
        else:
            image, rect = utilities.load_image(os.path.join('images', 'empty.jpg'))
        self.graveyardSprite.image = utilities.scale_to_small(image, rect)[0]

    def cancelDragging(self):
        self.draggingCard = None

    def returnToDeck(self, card):
        pass

    def sendToGraveyard(self, card):
        victim = MinimalCard(card.abbreviation, card.index)
        self.graveyard.append(victim)
        self.graveyardSprite.image = utilities.scale_to_small(card.image, card.rect)[0]
        card.position = client.GRAVEYARD
        clickHandler.removeClickable(card)
    
    def removeCardFromGraveyard(self, cardToRemove):
        allCards = [card for card in self.graveyard if (card.abbreviation == cardToRemove.abbreviation and card.index == cardToRemove.index)]
        try:
            self.graveyard.remove(allCards[0])
        except:
            print "Could not remove card %s from graveyard %s" % (cardToRemove, self.graveyard)  # TODO: FIGURE OUT THIS ERROR
    
    def removeCardFromDeck(self, cardToRemove):
        allCards = [card for card in self.deck.cards if (card.abbreviation == cardToRemove.abbreviation and card.index == cardToRemove.index)]
        self.deck.cards.remove(allCards[0])
    
    def sendToHand(self, card):
        originalPos = card.position  # this is changed by the call to client.moveCard, and I want the same value to be sent to the opponents
        self.moveCard(originalPos, client.HAND, card.tapped, card=card)
        self.client.moveCard(card.abbreviation, card.index, originalPos, client.HAND)
    
    def sendToLibrary(self, card, position = 0):
        #self.moveCard(card.position, client.DECK, card.tapped, card=card)
        card.parent.removeCard(card)
        if position >= 0:
            self.deck.cards.insert(position,MinimalCard(card.abbreviation, card.index))
        else:
            self.deck.cards.append(MinimalCard(card.abbreviation, card.index))
        self.setDeckSize()
        self.client.moveCard(card.abbreviation, card.index, card.position, client.DECK)
    
    def exile(self, card):
        card.parent.removeCard(card)
        self.client.moveCard(card.abbreviation, card.index, card.position, client.EXILE)
    
    def moveCard(self, originalPosition, newPosition, tapped=False, card=None):
        if originalPosition is client.DECK:
            if not self.isOpponent:
                self.removeCardFromDeck(card)
                if self.battle.visor is not None and self.battle.visor.group == "deckVisor":
                    self.battle.visor.loadDeck(self.deck)
            self.setDeckSize()
        if originalPosition is client.GRAVEYARD:
            self.removeCardFromGraveyard(card)
            self.updateGraveyardImage()
            if self.battle.visor is not None and self.battle.visor.group == "graveyardVisor":
                self.battle.visor.loadGraveyard(self.graveyard)
        if originalPosition >= 0:
            originalScroller = self.creatureScroller
            originalPositionInScroller = originalPosition
            if (originalPosition % 2) == 1:
                originalScroller = self.landScroller
                originalPositionInScroller -= 1
            originalPositionInScroller /= 2
        if newPosition >= 0:
            newScroller = self.creatureScroller
            newPositionInScroller = newPosition
            if (newPosition % 2) == 1:
                newScroller = self.landScroller
                newPositionInScroller -= 1
            newPositionInScroller /= 2
        if originalPosition >= 0:
            try:
                card = originalScroller.cards[originalPositionInScroller]
            except Exception, e:
                print e
                print "previous exception happened when moveCard called on player %s w/ arguments (%s, %s, %s, %s)" % (self.playerID, originalPosition, newPosition, tapped, card)
                return
            if originalPosition is newPosition:
                card.setTapped(tapped, notify=False)
                originalScroller.makeBG()
                return
            else:
                originalScroller.removeCard(card)
        if newPosition >= 0:
            card.setTapped(tapped)
            newScroller.addCard(card, newPositionInScroller)
        elif newPosition is client.GRAVEYARD:
            if originalPosition is client.HAND:
                card.parent = self.battle.hand.scroller
            self.sendToGraveyard(card)
        elif newPosition is client.HAND and not self.isOpponent:
            if card is None:
                card = Card(card.abbreviation, card.index, card.delegate, True)
            self.hand.insert(0,card)
            self.battle.refreshHand()
        elif newPosition is client.DECK:
            self.deckSize += 1
            self.setDeckSize()
        
        # Hand size calculations
        if newPosition is client.HAND:
            self.handSize += 1
            self.setName(self.name)
        if originalPosition is client.HAND:
            self.handSize -= 1
            self.setName(self.name)
    
    def untapAll(self):
        for scroller in self.scrollers:
            for card in scroller.cards:
                card.setTapped(False)
    
    def buttonClicked(self, position, sender, button):
        if sender is self.deckSprite and not self.isOpponent:
            if button is 1:
                self.drawCard()
            elif button is 3:
                contextMenu = ContextMenu(self, [["View Library",self.showDeck],["Shuffle",self.deck.shuffle]], position=position)
        elif sender is self.graveyardSprite and button is 3 and not self.isOpponent:
            ContextMenu(self, [["View Graveyard", self.showGraveyard]], position=position)
    
    def drawCard(self, showHand = True):
        abbreviation, index = self.deck.drawCard()
        if abbreviation is -1 and index is -1:
            #easygui.msgbox("You're out of cards!")
            print "Out of cards!"
            return
        newCard = Card(abbreviation, index, self, big=True)
        newCard.position = client.HAND
        self.hand.insert(0,newCard)
        self.battle.refreshHand()
        if showHand:
            self.battle.showHand()
        self.client.moveCard(abbreviation, index, client.DECK, client.HAND)
        self.setDeckSize()
        return abbreviation, index
    
    def hideContextMenu(self):
        self.contextMenu = None
    
    def showDeck(self):
        visor = DeckVisor(self.battle, self)
        visor.loadDeck(self.deck)
        self.battle.setVisor(visor)
    
    def showGraveyard(self):
        visor = GraveyardVisor(self.battle, self)
        visor.loadGraveyard(self.graveyard)
        self.battle.setVisor(visor)