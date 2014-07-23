# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deckEditor.ui'
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

class Ui_DeckEditor(object):
    def setupUi(self, DeckEditor):
        DeckEditor.setObjectName(_fromUtf8("DeckEditor"))
        DeckEditor.resize(705, 534)
        self.verticalLayout = QtGui.QVBoxLayout(DeckEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pteDeckEditor = QtGui.QPlainTextEdit(DeckEditor)
        self.pteDeckEditor.setObjectName(_fromUtf8("pteDeckEditor"))
        self.verticalLayout.addWidget(self.pteDeckEditor)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOpen = QtGui.QPushButton(DeckEditor)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.horizontalLayout.addWidget(self.btnOpen)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSave = QtGui.QPushButton(DeckEditor)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DeckEditor)
        QtCore.QMetaObject.connectSlotsByName(DeckEditor)

    def retranslateUi(self, DeckEditor):
        DeckEditor.setWindowTitle(_translate("DeckEditor", "Heavenly Inferno", None))
        self.btnOpen.setText(_translate("DeckEditor", "Open", None))
        self.btnSave.setText(_translate("DeckEditor", "Save", None))

