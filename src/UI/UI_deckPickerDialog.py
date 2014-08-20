# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deckPickerDialog.ui'
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

class Ui_DeckPickerDialog(object):
    def setupUi(self, DeckPickerDialog):
        DeckPickerDialog.setObjectName(_fromUtf8("DeckPickerDialog"))
        DeckPickerDialog.resize(559, 447)
        self.verticalLayout = QtGui.QVBoxLayout(DeckPickerDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lvDecks = QtGui.QListView(DeckPickerDialog)
        self.lvDecks.setObjectName(_fromUtf8("lvDecks"))
        self.verticalLayout.addWidget(self.lvDecks)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnChoose = QtGui.QPushButton(DeckPickerDialog)
        self.btnChoose.setObjectName(_fromUtf8("btnChoose"))
        self.horizontalLayout.addWidget(self.btnChoose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DeckPickerDialog)
        QtCore.QObject.connect(self.btnChoose, QtCore.SIGNAL(_fromUtf8("clicked()")), DeckPickerDialog.accept)
        QtCore.QObject.connect(self.lvDecks, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), DeckPickerDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DeckPickerDialog)

    def retranslateUi(self, DeckPickerDialog):
        DeckPickerDialog.setWindowTitle(_translate("DeckPickerDialog", "Pick a Deck", None))
        self.btnChoose.setText(_translate("DeckPickerDialog", "Choose This Deck", None))

