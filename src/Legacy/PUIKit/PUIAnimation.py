from PUITimeline import PUITimeline
import pygame

class PUIAnimation:
    def __init__(self, duration=1, delegate=None):
        self.timelines = {}
        self.currentTime = 0
    
    def update(self, dt):
        pass
    
    def setProperty(self, seconds, property, value, target):
        try:
            timeline = self.timelines[property]
        except:
            timeline = PUITimeline(property, target)
        timeline.setValueAtTime(seconds, value)