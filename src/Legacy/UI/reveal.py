import pygame
from util import utilities
from Displayable import Displayable
import clickHandler

class Reveal:
    def __init__(self, card, playerName, battle):
        self.card = card
        self.card.rect.center = (640,512)
        self.shaderLayer = pygame.Surface((1280,1024))
        self.shaderLayer.set_alpha(184)
        self.shaderLayer.fill((0,0,0))
        clickHandler.setModal(self)
        self.battle = battle
        self.battle.setContextMenu(self) # Should just work - no right click during a reveal
        
        self.nameFont = pygame.font.Font(None,20)
        text = "%s reveals:" % (playerName)
        self.nameRect = pygame.Rect((0,0), self.nameFont.size(text))
        self.nameRect.midbottom = (self.card.rect.midtop[0], self.card.rect.midtop[1] - 10)
        self.nameSurface = self.nameFont.render(text, True, (255,255,255))
        
    def click(self, position, button):
        clickHandler.setModal(None)
        self.battle.setContextMenu(None)
    
    
    def draw(self, screen):
        screen.blit(self.shaderLayer, (0,0))
        screen.blit(self.card.image, self.card.rect.topleft)
        screen.blit(self.nameSurface, self.nameRect.topleft)
    
    def move(self, position):
        pass
    def endClick(self, position):
        pass