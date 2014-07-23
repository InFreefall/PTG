# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created: Wed Feb 27 18:52:56 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QPlayer(object):
    def setupUi(self, QPlayer):
        QPlayer.setObjectName(_fromUtf8("QPlayer"))
        QPlayer.resize(783, 594)
        self.gridLayout = QtGui.QGridLayout(QPlayer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lvCreatures = QtGui.QListView(QPlayer)
        self.lvCreatures.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvCreatures.setDragEnabled(True)
        self.lvCreatures.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lvCreatures.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lvCreatures.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvCreatures.setFlow(QtGui.QListView.LeftToRight)
        self.lvCreatures.setObjectName(_fromUtf8("lvCreatures"))
        self.gridLayout.addWidget(self.lvCreatures, 0, 0, 1, 1)
        self.lvLands = QtGui.QListView(QPlayer)
        self.lvLands.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvLands.setDragEnabled(True)
        self.lvLands.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lvLands.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lvLands.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvLands.setFlow(QtGui.QListView.LeftToRight)
        self.lvLands.setObjectName(_fromUtf8("lvLands"))
        self.gridLayout.addWidget(self.lvLands, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.piPlayerInfo = QPlayerInfo(QPlayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.piPlayerInfo.sizePolicy().hasHeightForWidth())
        self.piPlayerInfo.setSizePolicy(sizePolicy)
        self.piPlayerInfo.setObjectName(_fromUtf8("piPlayerInfo"))
        self.horizontalLayout.addWidget(self.piPlayerInfo)
        self.vlDeck = QtGui.QVBoxLayout()
        self.vlDeck.setObjectName(_fromUtf8("vlDeck"))
        self.btnDeck = QCardPileButton(QPlayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeck.sizePolicy().hasHeightForWidth())
        self.btnDeck.setSizePolicy(sizePolicy)
        self.btnDeck.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.btnDeck.setAcceptDrops(True)
        self.btnDeck.setIconSize(QtCore.QSize(16, 278))
        self.btnDeck.setFlat(True)
        self.btnDeck.setObjectName(_fromUtf8("btnDeck"))
        self.vlDeck.addWidget(self.btnDeck)
        self.lblDeckSize = QtGui.QLabel(QPlayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDeckSize.sizePolicy().hasHeightForWidth())
        self.lblDeckSize.setSizePolicy(sizePolicy)
        self.lblDeckSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDeckSize.setObjectName(_fromUtf8("lblDeckSize"))
        self.vlDeck.addWidget(self.lblDeckSize)
        self.horizontalLayout.addLayout(self.vlDeck)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.btnGraveyard = QCardPileButton(QPlayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGraveyard.sizePolicy().hasHeightForWidth())
        self.btnGraveyard.setSizePolicy(sizePolicy)
        self.btnGraveyard.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.btnGraveyard.setAcceptDrops(True)
        self.btnGraveyard.setIconSize(QtCore.QSize(16, 278))
        self.btnGraveyard.setFlat(True)
        self.btnGraveyard.setObjectName(_fromUtf8("btnGraveyard"))
        self.gridLayout.addWidget(self.btnGraveyard, 0, 1, 1, 1)
        self.lblCommander = QtGui.QLabel(QPlayer)
        self.lblCommander.setObjectName(_fromUtf8("lblCommander"))
        self.gridLayout.addWidget(self.lblCommander, 0, 2, 2, 1)

        self.retranslateUi(QPlayer)
        QtCore.QMetaObject.connectSlotsByName(QPlayer)

    def retranslateUi(self, QPlayer):
        QPlayer.setWindowTitle(_translate("QPlayer", "Form", None))
        self.btnDeck.setText(_translate("QPlayer", "DECK", None))
        self.lblDeckSize.setText(_translate("QPlayer", "0 Cards in Deck", None))
        self.btnGraveyard.setText(_translate("QPlayer", "GRAVEYARD", None))
        self.lblCommander.setText(_translate("QPlayer", "YOUR COMMANDER HERE", None))

from QCardPileButton import QCardPileButton
from QPlayerInfo import QPlayerInfo
