'''
Created on Jul 19, 2011

@author: mitchell
'''

from UI.UI_visualDeckEditor import Ui_visualDeckEditor
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, QString
from QItemPicker import QItemPicker
from Models.QDeckListModel import QDeckListModel
from statedb import Database, CardLookupException
from flowlayout import FlowLayout
import json
import os
import urllib

class QVisualDeckEditor(QDialog, Ui_visualDeckEditor):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.deck = {}

        imagesDir = os.path.join('..', 'images')
        self.tabWidget.setTabIcon(0,
                QIcon(os.path.join(imagesDir, 'mana', 'red64.png')))
        self.tabWidget.setTabText(0, "")
        self.setUpTab(self.tabRed, "red")
        
        self.tabWidget.setTabIcon(1,
                QIcon(os.path.join(imagesDir, 'mana', 'green64.png')))
        self.tabWidget.setTabText(1, "")
        self.setUpTab(self.tabGreen, "green")
        
        self.tabWidget.setTabIcon(2,
                QIcon(os.path.join(imagesDir, 'mana', 'blue64.png')))
        self.tabWidget.setTabText(2, "")
        self.setUpTab(self.tabBlue, "blue")
        
        self.tabWidget.setTabIcon(3,
                QIcon(os.path.join(imagesDir, 'mana', 'white64.png')))
        self.tabWidget.setTabText(3, "")
        self.setUpTab(self.tabWhite, "white")
        
        self.tabWidget.setTabIcon(4,
                QIcon(os.path.join(imagesDir, 'mana', 'black64.png')))
        self.tabWidget.setTabText(4, "")
        self.setUpTab(self.tabBlack, "black")

        self.setUpTab(self.tabMulticolor, "multicolor")
        self.setUpTab(self.tabColorless, "colorless")

        self.setExpansion("M15")

    def setExpansion(self, expansion):
        f = open("json/M15.json")
        j = json.loads(f.read())
        f.close()
        cards = j['cards']

        for (color, tab) in [('Red',   self.tabRed),
                             ('Green', self.tabGreen),
                             ('Blue',  self.tabBlue),
                             ('Black', self.tabBlack),
                             ('White', self.tabWhite)]:
            def filterFunc(card):
                try:
                    return card['colors'] == [color]
                except:
                    # colorless
                    return False
            cardsOfColor = filter(filterFunc, cards)
                
            for card in cardsOfColor[:2]:
                if color != 'Red':
                    break
                cardURL = "http://mtgimage.com/multiverseid/%s.jpg" % \
                          (card['multiverseid'])
                label = QLabel()
                data = urllib.urlopen(cardURL).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                label.setPixmap(pixmap)
                tab.layout.addWidget(label)
        
    def setUpTab(self, tab, todoCardFilter=None):
        #QLabel(todoCardFilter, tab)
        
        tab.layout = FlowLayout(tab)
        # for i in range(25):
        #     btn = QPushButton()
        #     btn.pixmap = QPixmap(os.path.join('cards','m14','128.jpg'))
        #     grid.addWidget(btn)#QLabel(todoCardFilter + str(i)))
        #     #QLabel(todoCardFilter + str(i), grid)

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    d = QVisualDeckEditor()
    d.show()
    d.raise_()
    app.exec_()
