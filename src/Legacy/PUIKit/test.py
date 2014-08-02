import pygame
from PUIWindow import PUIWindow
from pygame.locals import *
from PUILabel import PUILabel
from PUIButton import PUIButton
from PUITimeline import PUITimeline

class Battle:
    def __init__(self):
        self.window = PUIWindow((1280,1024), "Plamann: the Gathering")
        self.x = PUIButton("Hi! How are you this fine morning?", self)
        timeline = PUITimeline(self.x.rect, "center")
        timeline.setValueAtTime(0, (0,0))
        timeline.setValueAtTime(2, (1000,1000))
        timeline.setValueAtTime(3, self.window.rect.center)
        self.window.addSubview(self.x)

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            clock.tick(60)
            events = pygame.event.get()
            self.window.update(events, clock.get_time()/1000.0)
            for event in events:
                if event.type is QUIT:
                    print "Thank you for playing! Closing now..."
                    self.client.disconnect()
                    sys.exit()
                elif event.type is KEYDOWN and event.key is K_f:
                    self.window.toggleFullscreen()

pygame.init()
b = Battle()
b.run()