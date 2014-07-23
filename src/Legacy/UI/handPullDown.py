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

class HandPullDown(Visor):
    def __init__(self, battle, battleUIGroup, position=client.HAND):
        self.hidden = True
        self.battle = battle
        self.position = position
        
        self.group = "hand"
        
        self.surface = pygame.surface.Surface((1280, 500))
        self.scroller = CardScroller(pygame.rect.Rect(0,0,1280,455),self,self.group,bigCards=True)
        self.scroller.positionMod = -1
        self.scroller.setTappable(False)
        clickHandler.setClickable(self.group, False)
        if position is client.HAND:
            self.hideButton = Button(os.path.join("images","downArrow.png"), self, battleUIGroup)
            self.hideButton.rect.topleft = (30,0)
        elif position is client.DECK:
            self.hidden = False
            self.hideButton = Button(os.path.join("images","deckArrow.png"), self, self.group)
            self.hideButton.rect.topright = (1280,475)
            clickHandler.setClickable(self.group, True)

    def draw(self, surface):
        if not self.hidden:
            self.scroller.draw(self.surface)
            self.surface.blit(self.hideButton.image, self.hideButton.rect.topleft)
            surface.blit(self.surface, (0,0))
        else:
            surface.blit(self.hideButton.image, self.hideButton.rect.topleft)

    def toggleHidden(self):
        self.hideButton.image = pygame.transform.flip(self.hideButton.image, False, True)
        if self.hidden:
            self.hideButton.rect.topleft = (30,475)
            clickHandler.setClickable(self.group, True)
        else:
            self.hideButton.rect.topleft = (30,0)
            clickHandler.setClickable(self.group, False)
        self.hidden = not self.hidden
        # IN the deck pulldown: self.battle.setVisor(None)

    def buttonClicked(self, position, sender, button):
        if button is 1:
            self.toggleHidden()
    
    def toggleClicked(self, index, sender):
        print "Toggle button clicked: %d" % (index)