from PUILabel import PUILabel
from PUIView import PUIView
import PUIClickHandler
import pygame
import pdb

class PUIButton(PUIView):
    def __init__(self, text, deleagte, padding=10, group="UI", button=1):
        self.label = PUILabel(text)
        self.rect = self.label.rect.inflate(2*padding,2*padding)
        self.rect.topleft = (0,0)
        PUIView.__init__(self, rect=self.rect, bgColor=(125,125,125))
        self.label.rect.center = self.rect.center
        print self.rect, self.label.rect
        self.addSubview(self.label)
        
        PUIClickHandler.addClickable(self, group, button)
    
    def click(self, position, button):
        #self.delegate.buttonClicked(position, self, button)
        print "Click!"
        pass

    def move(self, position):
        pass

    def endClick(self, position):
        pass