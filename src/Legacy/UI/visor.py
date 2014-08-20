import clickHandler
import pygame
import util
import os
from cardScroller import CardScroller
from Displayable import Displayable
from button import Button
from util import utilities

class Visor(Displayable):
    def __init__(self, battle, group):
        self.hidden = True
        self.battle = battle
        self.group = group
        self.surface = pygame.surface.Surface((1280, 500))
        self.scroller = CardScroller(pygame.rect.Rect(0,0,1280,455),self,self.group,bigCards=True)
        self.scroller.positionMod = -1
        self.scroller.setTappable(False)

    def update(self, event):
        if not self.hidden:
            self.scroller.update(event)

    def absoluteRect(self):
        return pygame.rect.Rect(0,0,self.surface.get_width(),self.surface.get_height())
    
    def addCard(self, card, position=0):
        self.scroller.addCard(card, position)
    
    def toggleHidden(self):
        raise NotImplementedException("Thingie")