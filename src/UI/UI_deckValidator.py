# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deckValidator.ui'
#
# Created: Thu Jul 24 01:13:39 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DeckValidatorDialog(object):
    def setupUi(self, DeckValidatorDialog):
        DeckValidatorDialog.setObjectName(_fromUtf8("DeckValidatorDialog"))
        DeckValidatorDialog.resize(938, 546)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(DeckValidatorDialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblCurrentDeck = QtGui.QLabel(DeckValidatorDialog)
        self.lblCurrentDeck.setObjectName(_fromUtf8("lblCurrentDeck"))
        self.verticalLayout.addWidget(self.lblCurrentDeck)
        self.tvIssues = QtGui.QTreeView(DeckValidatorDialog)
        self.tvIssues.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tvIssues.setObjectName(_fromUtf8("tvIssues"))
        self.verticalLayout.addWidget(self.tvIssues)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSelectDeck = QtGui.QPushButton(DeckValidatorDialog)
        self.btnSelectDeck.setObjectName(_fromUtf8("btnSelectDeck"))
        self.horizontalLayout.addWidget(self.btnSelectDeck)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOK = QtGui.QPushButton(DeckValidatorDialog)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.horizontalLayout.addWidget(self.btnOK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(DeckValidatorDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.bgManaCurve = QBarGraph(DeckValidatorDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgManaCurve.sizePolicy().hasHeightForWidth())
        self.bgManaCurve.setSizePolicy(sizePolicy)
        self.bgManaCurve.setObjectName(_fromUtf8("bgManaCurve"))
        self.verticalLayout_2.addWidget(self.bgManaCurve)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(DeckValidatorDialog)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL(_fromUtf8("clicked()")), DeckValidatorDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DeckValidatorDialog)

    def retranslateUi(self, DeckValidatorDialog):
        DeckValidatorDialog.setWindowTitle(_translate("DeckValidatorDialog", "Dialog", None))
        self.lblCurrentDeck.setText(_translate("DeckValidatorDialog", "INSERT_CURRENT_DECK_HERE", None))
        self.btnSelectDeck.setText(_translate("DeckValidatorDialog", "Select Deck", None))
        self.btnOK.setText(_translate("DeckValidatorDialog", "OK", None))
        self.label.setText(_translate("DeckValidatorDialog", "Mana Curve:", None))

from QBarGraph import QBarGraph
