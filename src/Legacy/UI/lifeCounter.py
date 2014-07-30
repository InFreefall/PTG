from button import Button
import os
import pygame

class LifeCounter(Button):
    def __init__(self, parent, client, group):
        Button.__init__(self, os.path.join('images','lifeCounter.png'), None, group=group, parent=parent)
        self.client = client
        self.background = self.image.copy()
        self.setLife(20)
        self.clickableZones = [(0,30), (95,30)]
    
    def setLife(self, life):
        self.life = life
        self.client.setLife(life)
        self.lifeLabel = pygame.font.Font(None,75).render(str(self.life), True, (200,0,0))
        self.image.blit(self.background, (0,0))
        self.image.blit(self.lifeLabel, (33,0))
    
    def click(self, position, button):
        if button is not 1:
            return
        rect = self.absoluteRect()
        x = position[0] - rect.x
        if 0 < x < 30:
            self.setLife(self.life - 1)
        elif 95 < x < 125:
            self.setLife(self.life + 1)