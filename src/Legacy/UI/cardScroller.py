import pygame
import clickHandler
import ezscroll
from CardContainer import CardContainer
from Displayable import Displayable
from card import Card
from ezscroll import ScrollBar
from pygame.locals import *
from util import utilities

class CardScroller(CardContainer, Displayable):
    def __init__(self, rect, parent, group, padding=5, bigCards=False, draggable=True):
        self.thick = 20
        self.surface = pygame.Surface((rect.size[0], rect.size[1] + self.thick))
        self.cards = []
        self.parent = parent
        self.group = group
        self.rect = rect
        self.maximumWidth = self.rect.width
        self.padding = padding
        self.positionMod = 0
        self.bigCards = bigCards
        self.draggable = draggable
        self.tappable = True
        self.makeBG()
        self.reloadScrollBar()

    def setDraggable(self, draggable):
        for card in self.cards:
            card.draggable = draggable
        self.draggable = draggable
    
    def setTappable(self, tappable):
        for card in self.cards:
            card.tappable = tappable
        self.tappable = tappable
    
    def setClickable(self, clickable):
        clickHandler.setClickable(self.group, clickable)
    
    def addCard(self, card, position=-1, returnToZero = False):
        if position is -1:
            self.cards.append(card)
        else:
            self.cards.insert(position, card)
        self.setCards(self.cards)
        # TODO: figure out how to have returnTozero work
    
    def setCards(self, cards):
        self.cards = cards
        for i,card in enumerate(cards):
            card.tappable = self.tappable
            card.draggable = self.draggable
            if (card.image.get_size() != utilities.smallCardSize and card.image.get_size() != utilities.smallCardSizeTapped) and not self.bigCards:
                card.setImage(card.abbreviation, card.index, big=False)
            elif self.bigCards and (card.image.get_size() == utilities.smallCardSize or card.image.get_size() == utilities.smallCardSizeTapped):
                card.setImage(card.abbreviation, card.index, big=True)
            card.parent = self
            if self.positionMod >= 0:
                card.position = i * 2 + self.positionMod
            else:
                card.position = self.positionMod
            clickHandler.removeClickable(card)
            clickHandler.addClickable(card, self.group)
        self.updateCardRects()
    
    def removeCard(self, card):
        card.parent = None
        self.cards.remove(card)
        self.setCards(self.cards)
        clickHandler.removeClickable(card)

    def makeBG(self):
        self.bg = pygame.Surface(self.rect.size)
        self.bg.fill((150,150,150))

    def updateCardRects(self):
        leftOfNextCard = self.padding
        for card in self.cards:
            card.rect.topleft = (leftOfNextCard, self.padding)
            leftOfNextCard += (self.padding + card.rect.width)
        if leftOfNextCard > self.rect.width:
            self.maximumWidth = leftOfNextCard
        else:
            self.maximumWidth = self.rect.width
        self.reloadScrollBar()

    def draw(self, surface):
        self.scrollBar.draw(self.surface)
        self.surface.blit(self.bg,(0,0))
        for card in self.cards:
            cardRect = card.rect.move(-self.scrollBar.get_scrolled()[0],0)
            if cardRect.right > self.rect.left and cardRect.left < self.rect.right:
                self.surface.blit(card.image, cardRect.topleft)
        surface.blit(self.surface, self.rect.topleft)

    def update(self, event):
        if (event is not None) and (event.type in (MOUSEBUTTONDOWN,MOUSEMOTION,MOUSEBUTTONUP)):
            originalPosition = event.pos
            absRect = self.rect.move(self.parent.absoluteRect().topleft)
            newPosition = (originalPosition[0] - absRect.x, originalPosition[1] - absRect.y - absRect.height)
            event.dict['pos'] = newPosition
            self.scrollBar.update(event)
            event.dict['pos'] = originalPosition

    def reloadScrollBar(self):
        try:
            self.scrollBar.setWorldWidth(self.maximumWidth)
        except:
            scrollRect = pygame.Rect(0, self.rect.height, self.rect.width, self.thick)
            self.scrollBar = ScrollBar(
                pygame.sprite.RenderPlain(),
                self.maximumWidth,
                scrollRect,
                self.surface,
                0,
                (0,0,0,0),
                True,
                self.thick)

    def click(self, position):
        print "Ich bin clicked! at: ", self.positionInBG(position)

    def positionInBG(self, position):
        return (position[0] - self.scrollBar.get_scrolled()[0] * -1, position[1] - self.scrollBar.get_scrolled()[1] * -1)

    def absoluteRect(self):
        return self.rect.move(self.scrollBar.get_scrolled()[0] * -1, self.scrollBar.get_scrolled()[1] * -1).move(self.parent.absoluteRect().topleft)
