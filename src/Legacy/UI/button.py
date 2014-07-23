import pygame
from util import utilities
from Displayable import Displayable
import clickHandler

class Button(pygame.sprite.Sprite, Displayable):
    def __init__(self, filename, delegate, group, parent=None, size=None): # Delegate must implement buttonClicked(self, position, sender)
        if parent is None:
            parent = delegate
        self.parent = parent
        self.group = group
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utilities.load_image(filename)
        if size is not None:
            self.image = pygame.transform.smoothscale(self.image, size)
            self.rect.size = size
        self.delegate = delegate
        clickHandler.addClickable(self, group)

    def __del__(self):
        clickHandler.removeClickable(self)

    def click(self, position, button):
        self.delegate.buttonClicked(position, self, button)

    def move(self, position):
        pass

    def endClick(self, position):
        pass

    def absoluteRect(self):
        return self.rect.move(self.parent.absoluteRect().topleft)

class ToggleButton(Button): # A two-zone toggle button - must be divided exactly in half
    def click(self, position, button):
        if button is 1:
            rect = self.absoluteRect()
            if position[0] < rect.centerx:
                zone = 0
            else:
                zone = 1
            self.delegate.toggleClicked(zone, self)