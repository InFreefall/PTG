'''
Created on Jul 9, 2011

@author: mitchell
'''

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui  import QWidget, QMenu, QPixmap, QCursor
from UI.UI_player import Ui_QPlayer
from Models.QCardModel import QCardModel
from Models.QCard import QCard
from Models.QDeck import QDeck
from Models.QTokenListModel import QTokenListModel
import pickle
import Networking.QGameClient # For the enum values
from QItemPicker import QItemPicker
from util import utilities

padding = 10

class QPlayer(QWidget, Ui_QPlayer):
    def __init__(self, handModel, gameDialog, gameType, controllable, playerName, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.controllable = controllable
        self.name = playerName
        if gameType is utilities.kGameTypeYuGiOh:
            self.btnDeck.pixmap = QPixmap("images/yugiohBack.jpg")
            self.piPlayerInfo.setLife(8000)
            self.piPlayerInfo.hidePoison()
        else:
            self.btnDeck.pixmap = QPixmap("images/back.jpg")
        self.btnDeck.displaysTopCard = False
        self.btnDeck.enlargeFunction = gameDialog.enlargeCard
        self.btnGraveyard.pixmap = QPixmap("images/empty.jpg")
        self.btnGraveyard.enlargeFunction = gameDialog.enlargeCard
        self.btnGraveyard.controllable = controllable

        self.gameType = gameType
        if gameType is utilities.kGameTypeTwoHeadedGiant:
            self.piPlayerInfo.setLife(30)
        
        # Setup models
        self.creaturesModel = QCardModel(self, self.controllable, 140)
        self.creaturesModel.enlargeFunction = gameDialog.enlargeCard
        self.landsModel = QCardModel(self, self.controllable, 140)
        self.landsModel.enlargeFunction = gameDialog.enlargeCard
        self.graveyardModel = QCardModel(self, self.controllable)
        self.graveyardModel.enlargeFunction = gameDialog.enlargeCard
        self.handModel = handModel
        self.handModel.enlargeFunction = gameDialog.enlargeCard
        self.exileModel = QCardModel(self, self.controllable)
        self.exileModel.enlargeFunction = gameDialog.enlargeCard
        if self.gameType is not utilities.kGameTypeYuGiOh:
            self.deck = QDeck(self, controllable, game="Magic")
        else:
            self.deck = QDeck(self, controllable, game="Yu-Gi-Oh")
        self.deck.enlargeFunction = gameDialog.enlargeCard

        # Handle commander format
        if gameType is utilities.kGameTypeCommander:
            self.lblCommander.show()
        else:
            self.lblCommander.hide()
        
        # Connect Views and Models
        self.lvCreatures.setModel(self.creaturesModel)
        self.lvLands.setModel(self.landsModel)
        self.btnGraveyard.setModel(self.graveyardModel)
        
        self.gameDialog = gameDialog
        
        # Connect signals and slots
        if self.controllable:
            self.connect(self.btnDeck, SIGNAL("clicked()"), self.drawCard)
            self.connect(self.lvCreatures, SIGNAL('doubleClicked(QModelIndex)'), self.creaturesModel.toggleCardAtIndexTapped)
            self.connect(self.lvCreatures, SIGNAL('customContextMenuRequested(QPoint)'), self.creaturesModel.contextMenuFunction(self.lvCreatures, self, gameDialog, self))
            self.connect(self.lvLands, SIGNAL('doubleClicked(QModelIndex)'), self.landsModel.toggleCardAtIndexTapped)
            self.connect(self.lvLands, SIGNAL('customContextMenuRequested(QPoint)'), self.landsModel.contextMenuFunction(self.lvLands, self, gameDialog, self))
            self.connect(self.btnDeck, SIGNAL('customContextMenuRequested(QPoint)'), self.displayDeckMenu)
        
        self.connect(self.lvCreatures, SIGNAL("clicked(QModelIndex)"), self.enlargeCreature)
        self.connect(self.lvLands, SIGNAL("clicked(QModelIndex)"), self.enlargeLand)
        self.connect(self.btnGraveyard, SIGNAL('customContextMenuRequested(QPoint)'), self.displayGraveyardMenu)
        self.btnDeck.setContextMenuCallback(self.displayDeckDragAndDropMenu)
        self.piPlayerInfo.hide()

    def setGameType(self, gameType):
        self.gameType = gameType

    
    def hideDeck(self):
        for i in range(0, self.vlDeck.count()):
            self.vlDeck.itemAt(i).widget().hide()
        self.piPlayerInfo.show()
    
    def flip(self):
        return
        flippedWidgets = []
        for row in range(0,self.layout().rowCount()):
            rowWidgets = []
            for column in range(0,self.layout().columnCount()):
                item = self.layout().itemAtPosition(row,column)
                rowWidgets.append(item)
                self.layout().removeItem(item)
            flippedWidgets.insert(0, rowWidgets)
        for y,row in enumerate(flippedWidgets):
            for x,widget in enumerate(row):
                self.layout().addItem(widget, y, x)
    
    def drawCard(self):
        abbreviation, index = self.deck.drawCard()
        self.handModel.addItem(QCard(abbreviation, index))

    def setDeckFromFile(self,filename):
        print "Loading deck %s..." % filename
        import os; print os.getcwd()
        self.deck.loadFromFile(filename)
        self.setupDeck()

    def setRandomDeckFromColors(self, colors):
        self.deck.randomFromColors(colors)
        self.setupDeck()

    def setupDeck(self):
        self.updateDeckSize()
        self.btnDeck.setModel(self.deck)
        self.connect(self.deck, SIGNAL('rowsInserted(QModelIndex,int,int)'), self.updateDeckSize)
        self.connect(self.deck, SIGNAL('rowsRemoved(QModelIndex,int,int)'), self.updateDeckSize)
        if self.gameType is utilities.kGameTypeCommander:
            commanderCard = self.deck.removeCommanderFromDeck()
            if commanderCard is not None:
                self.lblCommander.setPixmap(commanderCard.pixmap())
        
    def updateDeckSize(self, ignored1=None,ignored2=None,ignored3=None):
        self.lblDeckSize.setText("%d Cards in Deck" % (len(self.deck.list)))
    
    def enlargeLand(self, index):
        self.gameDialog.enlargeCard(self.landsModel.list[index.row()])
    
    def enlargeCreature(self, index):
        self.gameDialog.enlargeCard(self.creaturesModel.list[index.row()])
    
    def untapAll(self):
        self.creaturesModel.untapAll()
        self.landsModel.untapAll()
    
    def displayDeckMenu(self, pt):
        menu = QMenu()
        menu.addAction("Shuffle", self.deck.shuffle)
        menu.addAction("View Library", self.btnDeck.viewContents)
        menu.addAction("Reveal top card") # TODO: Implement

        def millFunction(number):
            def millCards():
                for i in range(number):
                    card = self.deck.list[-1]
                    self.deck.removeItem(card)
                    self.graveyardModel.addItem(card,0)
            return millCards
        millSubmenu = menu.addMenu("Mill")
        millSubmenu.addAction("Mill 1", millFunction(1))
        millSubmenu.addAction("Mill 2", millFunction(2))
        millSubmenu.addAction("Mill 3", millFunction(3))
        millSubmenu.addAction("Mill 5", millFunction(5))
        menu.exec_(self.btnDeck.mapToGlobal(pt))
    
    def displayGraveyardMenu(self, pt):
        menu = QMenu()
        menu.addAction("View Graveyard", self.btnGraveyard.viewContents)
        if self.controllable:
            menu.addAction("Exile All") #TODO: Implement
        menu.exec_(self.btnGraveyard.mapToGlobal(pt))
    
    def displayDeckDragAndDropMenu(self):
        print "Displaying menu"
        menu = QMenu()
        menu.addAction("Send to top")
        menu.addAction("Send to botton")
        result = menu.exec_(QCursor.pos())
        if result.text() == "Send to top":
            return len(self.deck.list)
        else:
            return 0 # Send to bottom
    
    def askToAddToken(self):
        picker = QItemPicker(self, self.addToken, QTokenListModel(self), "Token")
        picker.show()
    def addToken(self, filename):
        card = QCard('tokens',filename)
        self.creaturesModel.addItem(card)
    
    def displayExile(self):
        from PyQt4.QtGui import QListView, QAbstractItemView, QPushButton, QVBoxLayout, QLabel
        from PyQt4.QtCore import QSize
        from util import utilities
        windowSize = self.window().frameSize()
        self.viewer = QWidget(self.window())
        self.viewer.move(10,10)
        self.viewer.resize(QSize(windowSize.width()-(25+utilities.bigCardSize[0]),275))
        
        lvViewer = QListView(self.viewer)
        lvViewer.setModel(self.model)
        lvViewer.setDragEnabled(True)
        lvViewer.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        lvViewer.setFlow(QListView.LeftToRight)
        lvViewer.setFocus()
        self.connect(lvViewer, SIGNAL('clicked(QModelIndex)'), self.enlarge)
        
        button = QPushButton("Close", self.viewer)
        self.connect(button,SIGNAL('clicked()'),self.hideViewer)
        
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("I'm sorry this is so ugly.",self.viewer))
        layout.addWidget(lvViewer)
        layout.addWidget(button)
        self.viewer.setLayout(layout)
        
        self.viewer.show()
    
    ##################################
    #### Networking Methods ##########
    #### Called by QPTG     ##########
    ##################################
    
    def addCardTo(self, pickledCard, zone, position):
#        card = pickle.loads(pickledCard)
        card = QCard.unserializeCard(pickledCard)
        if int(zone) is Networking.QGameClient.HAND:
            self.piPlayerInfo.setHandSize(self.piPlayerInfo.handSize()+1)
        if int(zone) is Networking.QGameClient.DECK:
            self.piPlayerInfo.setDeckSize(self.piPlayerInfo.deckSize()+1)
        if int(zone) is Networking.QGameClient.EXILE:
            self.exileModel.addItem(card, int(position))
        if int(zone) is Networking.QGameClient.GRAVEYARD:
            self.graveyardModel.addItem(card, int(position))
        if int(zone) is Networking.QGameClient.CREATURES:
            self.creaturesModel.addItem(card, int(position))
        if int(zone) is Networking.QGameClient.LANDS:
            self.landsModel.addItem(card, int(position))
    
    def removeCardFrom(self, zone, position):
        if int(zone) is Networking.QGameClient.HAND:
            self.piPlayerInfo.setHandSize(self.piPlayerInfo.handSize()-1)
        if int(zone) is Networking.QGameClient.DECK:
            self.piPlayerInfo.setDeckSize(self.piPlayerInfo.deckSize()-1)
        if int(zone) is Networking.QGameClient.EXILE:
            self.exileModel.removeItem(self.exileModel.list[int(position)])
        if int(zone) is Networking.QGameClient.GRAVEYARD:
            self.graveyardModel.removeItem(self.graveyardModel.list[int(position)])
        if int(zone) is Networking.QGameClient.CREATURES:
            self.creaturesModel.removeItem(self.creaturesModel.list[int(position)])
        if int(zone) is Networking.QGameClient.LANDS:
            self.landsModel.removeItem(self.landsModel.list[int(position)])
    
    def setCardTo(self, pickledCard, zone, position):
        card = QCard.unserializeCard(pickledCard)
        if int(zone) is Networking.QGameClient.EXILE:
            self.exileModel.setItem(card, int(position))
        if int(zone) is Networking.QGameClient.GRAVEYARD:
            self.graveyardModel.setItem(card, int(position))
        if int(zone) is Networking.QGameClient.CREATURES:
            self.creaturesModel.setItem(card, int(position))
        if int(zone) is Networking.QGameClient.LANDS:
            self.landsModel.setItem(card, int(position))
