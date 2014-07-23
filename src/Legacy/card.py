from Networking import gameClient as client
import notificationCenter
import os
import pdb
import pygame
import settingsManager
import time
from contextMenu import ContextMenu
from easygui import *
from Displayable import Displayable
from util import utilities
from MinimalCard import MinimalCard

class Card(pygame.sprite.Sprite, Displayable):
    def __init__(self, abbreviation, index, delegate=None, big=False):
        pygame.sprite.Sprite.__init__(self)
        self.parent = None
        self.tapped = False
        self.tappable = True
        self.delegate = delegate
        self.draggingPosition = None
        self.clickedTime = 0
        self.setImage(abbreviation, index, big)
        self.position = 0
        self.draggable = True

    def setImage(self, abbreviation, index, big=False, bail=False):
        self.abbreviation, self.index = abbreviation, index
        path = ""
        if abbreviation == "back":
            path = os.path.join('images','back.jpg')
        elif abbreviation == "empty":
            path = os.path.join('images','empty.jpg')
        elif abbreviation == "tokens":
            path = os.path.join('images', 'tokens', str(index) + ".jpg")
        else:
            path = os.path.join(settingsManager.settings['cardsDir'], abbreviation, str(index) + ".jpg")
        oldRect = None
        try:
            oldRect = self.rect
        except AttributeError:
            pass
        try:
            self.image, self.rect = utilities.load_image(path)
        except Exception, e:
            if not bail:
                import cardCrawler
                cardCrawler.crawlCardAndInfo(abbreviation, index)
                return self.setImage(abbreviation, index, big, True)
            else:
                print "Cannot crawl card!"
                pdb.set_trace()
                raise e
        if oldRect is not None:
            self.rect = oldRect
        if (not big):
            self.image, self.rect = utilities.scale_to_small(self.image, self.rect)
        elif self.rect.size is not utilities.bigCardSize:
            self.image, self.rect = utilities.scale_to_big(self.image, self.rect)
        self.setTapped(self.tapped)

    def absoluteRect(self):
        if self.parent is None:
            return self.rect
        parentRect = self.parent.absoluteRect()
        return self.rect.move(parentRect.x, parentRect.y)

    def setTapped(self, tapped, notify=True):
        if (self.tapped == tapped):
            return
        modifier = -1
        if (self.tapped == True):
            modifier = 1
        self.tapped = tapped
        self.image = pygame.transform.rotate(self.image, modifier*90)
        self.rect.width, self.rect.height = self.rect.height, self.rect.width
        if notify:
            notificationCenter.postNotification("tapCard", self)
        try:
            self.parent.updateCardRects()
        except Exception, e:
            print e
            #pdb.set_trace()

    def toggleTapped(self):
        self.setTapped(not self.tapped)

    def getTapped(self):
        return self.tapped

    def doubleClick(self, position):
        if not self.tappable:
            return
        self.setTapped(not self.tapped)

    def click(self, position, button):
        if not self.parent.rect.move(self.parent.parent.absoluteRect().topleft).collidepoint(position):
            return False
        if button is 1:
            if (time.time() - self.clickedTime) <= 0.25:
                self.clickedTime = 0;
                self.delegate.cancelDragging()
                self.doubleClick(position)
                return
            else:
                self.clickedTime = time.time()
            if self.delegate is not None:
                notificationCenter.postNotification("changePlaceholder", MinimalCard(self.abbreviation,self.index))
            if not self.draggable:       # If card is not draggable
                return False
            self.clickedCoords = position
            self.draggingPosition = self.absoluteRect().topleft
            self.delegate.draggingCard = self
            return True
        elif button is 3 and self.draggable:
            list = []
            if self.position is not client.DECK:
                list.append(["Send To Library (Bottom)", self.sendToLibraryBottom])
                list.append(["Send To Library (Top)", self.sendToLibraryTop])
            if self.position is not client.HAND:
                list.append(["Send To Hand", self.sendToHand])
            if self.position < 0:
                list.append(["Reveal", self.reveal])
            list.append(["Exile", self.exile])
            ContextMenu(self, list, position=position)
            return True
            
    def sendToLibraryBottom(self):
        self.delegate.sendToLibrary(self,0)
    
    def sendToLibraryTop(self):
        self.delegate.sendToLibrary(self,-1)
    
    def sendToHand(self):
        self.delegate.sendToHand(self)
    
    def exile(self):
        self.delegate.exile(self)
    
    def reveal(self):
        self.delegate.client.reveal(self.abbreviation, self.index)
    
    def move(self, position):
        if not self.draggable:
            return
        try:
            self.draggingPosition = (self.draggingPosition[0] + (position[0] - self.clickedCoords[0]),  # Crashes if card is moved from deck to hand (this line)
                                     self.draggingPosition[1] + (position[1] - self.clickedCoords[1]))
            self.clickedCoords = position
        except:
            print "Error! Could not do the thingie!"

    def endClick(self, position):
        if not self.draggable:
            return
        self.delegate.endDragging(position)