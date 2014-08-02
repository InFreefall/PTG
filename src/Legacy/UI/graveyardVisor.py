import clickHandler
from Networking import gameClient as client
import pygame
import util
import os
from button import Button
from button import ToggleButton
from card import Card
from cardScroller import CardScroller
from visor import Visor

class GraveyardVisor(Visor):
    def __init__(self, battle, player):
        Visor.__init__(self, battle, "graveyardVisor")
        self.hidden = False
        self.player = player
        self.hideButton = Button(os.path.join("images","deckArrow.png"), self, self.group)
        self.hideButton.rect.topright = (1280,475)
        self.scroller.positionMod = client.GRAVEYARD
        clickHandler.setClickable(self.group, True)

    def draw(self, surface):
        self.scroller.draw(self.surface)
        self.surface.blit(self.hideButton.image, self.hideButton.rect.topleft)
        surface.blit(self.surface, (0,0))

    def toggleHidden(self):
        clickHandler.removeGroup(self.group)
        self.battle.setVisor(None)

    def buttonClicked(self, position, sender, button):
        if button is 1:
            self.toggleHidden()
    
    def toggleClicked(self, index, sender):
        print "Toggle button clicked: %d" % (index)
    
    def loadGraveyard(self, graveyard):
        for minimalCard in graveyard:
            card = Card(minimalCard.abbreviation, minimalCard.index, self.player, True)
            self.addCard(card)