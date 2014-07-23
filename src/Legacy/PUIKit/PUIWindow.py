import pdb
import pygame
from pygame.locals import *
import time

import PUIAnimationManager
import PUIClickHandler
from PUIView import PUIView

class PUIWindow(PUIView):
    def __init__(self, size, caption="PUIWindow", bgColor=(0,0,0), fullscreen=False):
        self.bgColor = bgColor
        self.superview = None
        self.image = pygame.display.set_mode(size)
        self.image.fill(bgColor)
        self.rect = pygame.Rect((0,0), size)
        self.setFullscreen(fullscreen)
        pygame.display.set_caption(caption)
        self.renderer = pygame.sprite.RenderUpdates()
        self.subviews = []
        self.lastTime = -1
    
    def update(self, events, dt):
        """if self.lastTime is -1:
            dt = 0
        else:
            dt = pygame.time.get_ticks() - self.lastTime
        self.lastTime = pygame.time.get_ticks()"""
        print dt
        PUIAnimationManager.update(dt)
        for subview in self.subviews:
            subview.updateAll(events, dt)
        self.draw()
        pygame.display.flip()
        for event in events:
            if event.type is MOUSEMOTION:
                PUIClickHandler.move(event.pos)
            elif event.type is MOUSEBUTTONDOWN:
                PUIClickHandler.click(event.pos, event.button)
            elif event.type is MOUSEBUTTONUP:
                PUIClickHandler.endClick(event.pos, event.button)
    
    def toggleFullscreen(self):
        self.setFullscreen(not self.fullscreen)
    
    def setFullscreen(self, fullscreen):
        self.fullscreen = fullscreen
        if fullscreen:
            self.image = pygame.display.set_mode(self.rect.size, FULLSCREEN)
        else:
            self.image = pygame.display.set_mode(self.rect.size)