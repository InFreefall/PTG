# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draftUI.ui'
#
# Created: Fri Jun 29 10:54:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DraftDialog(object):
    def setupUi(self, DraftDialog):
        DraftDialog.setObjectName(_fromUtf8("DraftDialog"))
        DraftDialog.resize(1476, 569)
        self.verticalLayout_3 = QtGui.QVBoxLayout(DraftDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lblRemaining = QtGui.QLabel(DraftDialog)
        self.lblRemaining.setObjectName(_fromUtf8("lblRemaining"))
        self.verticalLayout_3.addWidget(self.lblRemaining)
        self.lblSender = QtGui.QLabel(DraftDialog)
        self.lblSender.setObjectName(_fromUtf8("lblSender"))
        self.verticalLayout_3.addWidget(self.lblSender)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblWaiting = QtGui.QLabel(DraftDialog)
        self.lblWaiting.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWaiting.setObjectName(_fromUtf8("lblWaiting"))
        self.verticalLayout_2.addWidget(self.lblWaiting)
        self.lvCards = QtGui.QListView(DraftDialog)
        self.lvCards.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvCards.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvCards.setMovement(QtGui.QListView.Static)
        self.lvCards.setFlow(QtGui.QListView.LeftToRight)
        self.lvCards.setObjectName(_fromUtf8("lvCards"))
        self.verticalLayout_2.addWidget(self.lvCards)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.debugButton = QtGui.QPushButton(DraftDialog)
        self.debugButton.setObjectName(_fromUtf8("debugButton"))
        self.horizontalLayout.addWidget(self.debugButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnPass = QtGui.QPushButton(DraftDialog)
        self.btnPass.setObjectName(_fromUtf8("btnPass"))
        self.horizontalLayout.addWidget(self.btnPass)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btnAdd = QtGui.QPushButton(DraftDialog)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QPushButton(DraftDialog)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.verticalLayout.addWidget(self.btnRemove)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.lvDeck = QtGui.QListView(DraftDialog)
        self.lvDeck.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvDeck.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvDeck.setMovement(QtGui.QListView.Static)
        self.lvDeck.setFlow(QtGui.QListView.LeftToRight)
        self.lvDeck.setObjectName(_fromUtf8("lvDeck"))
        self.horizontalLayout_2.addWidget(self.lvDeck)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DraftDialog)
        QtCore.QMetaObject.connectSlotsByName(DraftDialog)

    def retranslateUi(self, DraftDialog):
        DraftDialog.setWindowTitle(QtGui.QApplication.translate("DraftDialog", "Draft", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRemaining.setText(QtGui.QApplication.translate("DraftDialog", "Remaining Packs: m11 wwk land", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSender.setText(QtGui.QApplication.translate("DraftDialog", "Nick passed:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWaiting.setText(QtGui.QApplication.translate("DraftDialog", "Waiting for the next pack to be passed...", None, QtGui.QApplication.UnicodeUTF8))
        self.debugButton.setText(QtGui.QApplication.translate("DraftDialog", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPass.setText(QtGui.QApplication.translate("DraftDialog", "Pass Pack", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("DraftDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setText(QtGui.QApplication.translate("DraftDialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))

