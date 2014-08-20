import pygame
from PUIView import PUIView

class PUILabel(PUIView):
    def __init__(self, text, font=None, bold=False, italic=False, size=20, color=(255,255,255)):
        PUIView.__init__(self, renderer=None)
        if font is not None:
            fontPath = pygame.font.match_font(font, bold, italic)
        else:
            fontPath = None
        self.font = pygame.font.Font(fontPath, size)
        self.color = color
        self.setText(text)
        
    def setText(self, text):
        self.rect = pygame.Rect((0,0),self.font.size(text))
        self.image = self.font.render(text, True, self.color)
        self.dirty = 1