'''
Created on Jul 10, 2011

@author: mitchell
'''

import os
from PyQt4.QtGui import QPixmap, QPainter, QBrush, QPen, QColor, QFont
from PyQt4.QtCore import Qt
import settingsManager
import cardCrawler
import statedb

class QCard(object):
    def __init__(self, abbreviation, index):
        self.abbreviation = abbreviation
        self.index = index
        self._pixmap = None
        self.tapped = False
        self._upsideDown = False
        self.isFlipCard = False
        self.plusOneCounter = 0
        try:
            statedb.commonDB().nameForAbbreviationIndex(abbreviation, "%s000"%(index))
            self.isFlipCard = True
        except TypeError:
            pass
    
    def __getstate__(self):  # For pickling support
        result = self.__dict__.copy()
        del result['_pixmap']
        return result
    
    def __setstate__(self, dict):
        self.__dict__ = dict
        self._pixmap = None
    
    def pixmap(self):
        if self._pixmap is None:
            if not self.upsideDown:
                if self.abbreviation == "tokens":
                    path = os.path.join(settingsManager.settings['imagesDir'],
                                        'tokens',
                                        self.index)
                else:
                    path = os.path.join(settingsManager.settings['cardsDir'],
                                        self.abbreviation,
                                        "%s.jpg"%(self.index))
                    pngPath = os.path.join(settingsManager.settings['cardsDir'],
                                        self.abbreviation,
                                        "%s.png"%(self.index))
                    print "Opening path {}".format(path)
                    if not os.path.isfile(path):
                        if os.path.isfile(pngPath):
                            print "Opening path {}".format(pngPath)
                            path = pngPath
                        else:
                            cardCrawler.crawlCardAndInfo(self.abbreviation, self.index)
            else: # Card is upside down
                if self.isFlipCard:
                    path = os.path.join(settingsManager.settings['cardsDir'],
                                        self.abbreviation,
                                        "%s000.jpg"%(self.index))
                else:
                    if not self.abbreviation.startswith('ygo'): # Is a Magic card
                        path = os.path.join(settingsManager.settings['imagesDir'],'back.jpg')
                    else: # Is a Yu-Gi-Oh card
                        path = os.path.join(settingsManager.settings['imagesDir'],'yugiohBack.jpg')
            # Resize card in case it is not already the correct height
            self._pixmap = QPixmap(path).scaledToHeight(445,Qt.SmoothTransformation)
            print "%s" % QPixmap(path).isNull()
        if self.plusOneCounter is not 0:
            painter = QPainter(self._pixmap)
            painter.setBrush(QBrush(Qt.darkBlue))
            painter.drawRect(0,60,130,45)
            painter.setPen(QPen(Qt.white))
            painter.setFont(QFont("Helvetica", 30, weight=QFont.Bold))
            text = "+%s/+%s" % (self.plusOneCounter,self.plusOneCounter)
            if (self.plusOneCounter < 0):
                text = "%s/%s" % (self.plusOneCounter,self.plusOneCounter)
            painter.drawText(5,97,text)
        # if self._pixmap is None or self._pixmap.isNull() and self.abbreviation == 'M15':
            # Get debug info from Dan. Currently, can not reproduce.
        return self._pixmap

    def bottomPixmap(self):
        """ If a card is flipped upside down, this function
        allows the owner of the card to see the bottom. """
        if not self.upsideDown:
            return self.pixmap()
        if self.abbreviation == "tokens":
            path = os.path.join(settingsManager.settings['imagesDir'],
                                'tokens',
                                self.index)
        else:
            path = os.path.join(settingsManager.settings['cardsDir'],
                                self.abbreviation,
                                "%s.jpg"%(self.index))
            if not os.path.isfile(path):
                cardCrawler.crawlCardAndInfo(self.abbreviation, self.index)
        return QPixmap(path).scaledToHeight(445,Qt.SmoothTransformation)

    def addPlusOne(self):
        self.plusOneCounter += 1
        self.updatePixmap()

    def removePlusOne(self):
        self.plusOneCounter -= 1
        self.updatePixmap()

    def updatePixmap(self):
        self._pixmap = None
        self.pixmap()
    
    def setUpsideDown(self, value):
        if value is not self._upsideDown:
            self._pixmap = None
        self._upsideDown = value
    def getUpsideDown(self):
        return self._upsideDown
    upsideDown = property(getUpsideDown, setUpsideDown)

    def serialized(self):
        abbreviation = self.abbreviation
        index = self.index
        plusOneCounter = str(self.plusOneCounter)
        tapped = "F"
        if self.tapped:
            tapped = "T"
        upsideDown = "F"
        if self.upsideDown:
            upsideDown = "T"
        isFlipCard = "F"
        if self.isFlipCard:
            isFlipCard = "T"
        return ','.join([abbreviation,index,tapped,upsideDown,isFlipCard,plusOneCounter])

    @classmethod
    def unserializeCard(cls, string):
        fields = string.split(',')
        result = QCard(fields[0],fields[1])
        result.tapped = (fields[2] == "T")
        result.upsideDown = (fields[3] == "T")
        result.isFlipCard = (fields[4] == "T")
        result.plusOneCounter = int(fields[5])
        return result
