import pygame

class PUIView(pygame.sprite.Sprite):
    def __init__(self, location, size):
        self.__init__(rect=pygame.Rect(location, size))
    
    def __init__(self, renderer=pygame.sprite.RenderUpdates(), bgColor=(0,0,0), rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.subviews = []
        self.renderer = renderer
        self.image = None
        self.rect = rect
        self.bgColor = bgColor
        if self.rect is not None:
            self.image = pygame.Surface(self.rect.size)
            self.image.fill(self.bgColor)
        self.superview = None
    
    def addSubview(self, subview):
        self.subviews.append(subview)
        self.renderer.add(subview)
    
    def updateAll(self, events, dt):
        for subview in self.subviews:
            subview.updateAll(events, dt)
        self.update(events, dt)
        self.draw()
    
    def update(self, events, dt):
        pass # Override this to do something useful
    
    def draw(self):
        if self.renderer is None:
            return
        def clearCallback(surf, rect):
            surf.fill(self.bgColor, rect)
        self.renderer.clear(self.image, clearCallback)
        self.renderer.draw(self.image)
    
    def absoluteRect(self):
        if self.superview is None:
            return self.rect
        topleft = self.superview.rect.topleft
        return self.rect.move(topleft[0], topleft[1])