# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createGameWindow.ui'
#
# Created: Mon May 27 16:48:56 2013
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

class Ui_NewGameDialog(object):
    def setupUi(self, NewGameDialog):
        NewGameDialog.setObjectName(_fromUtf8("NewGameDialog"))
        NewGameDialog.resize(672, 416)
        self.verticalLayout_3 = QtGui.QVBoxLayout(NewGameDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(NewGameDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gameName = QtGui.QLineEdit(NewGameDialog)
        self.gameName.setObjectName(_fromUtf8("gameName"))
        self.horizontalLayout_2.addWidget(self.gameName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(NewGameDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.cbGameType = QtGui.QComboBox(NewGameDialog)
        self.cbGameType.setObjectName(_fromUtf8("cbGameType"))
        self.cbGameType.addItem(_fromUtf8(""))
        self.cbGameType.addItem(_fromUtf8(""))
        self.cbGameType.addItem(_fromUtf8(""))
        self.cbGameType.addItem(_fromUtf8(""))
        self.cbGameType.addItem(_fromUtf8(""))
        self.cbGameType.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cbGameType)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.expansionLayout = QtGui.QVBoxLayout()
        self.expansionLayout.setObjectName(_fromUtf8("expansionLayout"))
        self.lblChosenExpansions = QtGui.QLabel(NewGameDialog)
        self.lblChosenExpansions.setObjectName(_fromUtf8("lblChosenExpansions"))
        self.expansionLayout.addWidget(self.lblChosenExpansions)
        self.lvExpansions = QtGui.QListView(NewGameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvExpansions.sizePolicy().hasHeightForWidth())
        self.lvExpansions.setSizePolicy(sizePolicy)
        self.lvExpansions.setObjectName(_fromUtf8("lvExpansions"))
        self.expansionLayout.addWidget(self.lvExpansions)
        self.btnSelectExpansions = QtGui.QPushButton(NewGameDialog)
        self.btnSelectExpansions.setObjectName(_fromUtf8("btnSelectExpansions"))
        self.expansionLayout.addWidget(self.btnSelectExpansions)
        self.horizontalLayout_5.addLayout(self.expansionLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.buttonBox = QtGui.QDialogButtonBox(NewGameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(NewGameDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewGameDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewGameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewGameDialog)

    def retranslateUi(self, NewGameDialog):
        NewGameDialog.setWindowTitle(_translate("NewGameDialog", "Dialog", None))
        self.label.setText(_translate("NewGameDialog", "Game Name:", None))
        self.gameName.setToolTip(_translate("NewGameDialog", "The name this game of PTG will appear under.", None))
        self.gameName.setText(_translate("NewGameDialog", "Username\'s Game", None))
        self.label_2.setText(_translate("NewGameDialog", "Game Type:", None))
        self.cbGameType.setItemText(0, _translate("NewGameDialog", "Constructed", None))
        self.cbGameType.setItemText(1, _translate("NewGameDialog", "Random Decks", None))
        self.cbGameType.setItemText(2, _translate("NewGameDialog", "Two-Headed Giant", None))
        self.cbGameType.setItemText(3, _translate("NewGameDialog", "Commander", None))
        self.cbGameType.setItemText(4, _translate("NewGameDialog", "Draft", None))
        self.cbGameType.setItemText(5, _translate("NewGameDialog", "Yu-Gi-Oh", None))
        self.lblChosenExpansions.setText(_translate("NewGameDialog", "Chosen Expansions:", None))
        self.btnSelectExpansions.setText(_translate("NewGameDialog", "Select Expansions", None))

