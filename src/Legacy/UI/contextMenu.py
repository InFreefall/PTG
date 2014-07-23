import clickHandler
import notificationCenter
import pygame
from Displayable import Displayable
from util import utilities

class ContextMenu(Displayable):
    def __init__(self, delegate, menuItems, padding=5, position=(0,0)): # menuItems is a list of strings
        self.menuItems = menuItems
        self.padding = padding
        self.delegate = delegate
        clickHandler.setModal(self)
        self.generateSurfaces()
        self.rect.topleft = position
        notificationCenter.postNotification(utilities.setContextMenu, self)
    
    def generateSurfaces(self):
        self.textSurfaces = []
        self.textRects = []
        font = pygame.font.Font(None,22)
        maxWidth = 0
        height = self.padding
        for item in self.menuItems:
            surface = font.render(item[0], True, (255,255,255))
            if surface.get_width() > maxWidth:
                maxWidth = surface.get_width() + 2 * self.padding
            self.textRects.append(pygame.Rect(self.padding,height,surface.get_width(),surface.get_height()))
            height += surface.get_height() + self.padding
            self.textSurfaces.append(surface)
        self.surface = pygame.Surface((maxWidth, height))
        self.rect = pygame.Rect(0,0,maxWidth,height)
    
    def draw(self, surface):
        self.surface.fill((100,100,100))
        currentHeight = self.padding
        for text in self.textSurfaces:
            self.surface.blit(text, (self.padding, currentHeight))
            currentHeight += text.get_height() + self.padding
        x = self.rect.x
        y = self.rect.y
        if x + self.surface.get_width() > pygame.display.Info().current_w:
            self.rect = self.rect.move(-self.surface.get_width(),0)
        if y + self.surface.get_height() > pygame.display.Info().current_h:
            self.rect = self.rect.move(0,-self.surface.get_height())
        surface.blit(self.surface, self.rect.topleft)
    
    def absoluteRect(self):
        return self.rect
    
    def click(self, position, button):
        for i,rect in enumerate(self.textRects):
            if rect.move(self.absoluteRect().topleft).collidepoint(position):
                #self.delegate.menuClicked(i)
                self.menuItems[i][1]()
                break
        notificationCenter.postNotification(utilities.setContextMenu, None)
        clickHandler.setModal(None)
    
    def move(self, position):
        pass
    
    def endClick(self, position):
        pass