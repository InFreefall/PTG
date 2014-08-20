# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opponentInfo.ui'
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

class Ui_OpponentInfo(object):
    def setupUi(self, OpponentInfo):
        OpponentInfo.setObjectName(_fromUtf8("OpponentInfo"))
        OpponentInfo.resize(321, 335)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OpponentInfo.sizePolicy().hasHeightForWidth())
        OpponentInfo.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(OpponentInfo)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblLifeLabel = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLifeLabel.sizePolicy().hasHeightForWidth())
        self.lblLifeLabel.setSizePolicy(sizePolicy)
        self.lblLifeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLifeLabel.setObjectName(_fromUtf8("lblLifeLabel"))
        self.verticalLayout.addWidget(self.lblLifeLabel)
        self.lblPoisonLabel = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPoisonLabel.sizePolicy().hasHeightForWidth())
        self.lblPoisonLabel.setSizePolicy(sizePolicy)
        self.lblPoisonLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPoisonLabel.setObjectName(_fromUtf8("lblPoisonLabel"))
        self.verticalLayout.addWidget(self.lblPoisonLabel)
        self.lblHandSizeLabel = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHandSizeLabel.sizePolicy().hasHeightForWidth())
        self.lblHandSizeLabel.setSizePolicy(sizePolicy)
        self.lblHandSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblHandSizeLabel.setObjectName(_fromUtf8("lblHandSizeLabel"))
        self.verticalLayout.addWidget(self.lblHandSizeLabel)
        self.lblDeckSizeLabel = QtGui.QLabel(OpponentInfo)
        self.lblDeckSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDeckSizeLabel.setObjectName(_fromUtf8("lblDeckSizeLabel"))
        self.verticalLayout.addWidget(self.lblDeckSizeLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblLife = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLife.sizePolicy().hasHeightForWidth())
        self.lblLife.setSizePolicy(sizePolicy)
        self.lblLife.setObjectName(_fromUtf8("lblLife"))
        self.verticalLayout_2.addWidget(self.lblLife)
        self.lblPoison = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPoison.sizePolicy().hasHeightForWidth())
        self.lblPoison.setSizePolicy(sizePolicy)
        self.lblPoison.setObjectName(_fromUtf8("lblPoison"))
        self.verticalLayout_2.addWidget(self.lblPoison)
        self.lblHandSize = QtGui.QLabel(OpponentInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHandSize.sizePolicy().hasHeightForWidth())
        self.lblHandSize.setSizePolicy(sizePolicy)
        self.lblHandSize.setObjectName(_fromUtf8("lblHandSize"))
        self.verticalLayout_2.addWidget(self.lblHandSize)
        self.lblDeckSize = QtGui.QLabel(OpponentInfo)
        self.lblDeckSize.setObjectName(_fromUtf8("lblDeckSize"))
        self.verticalLayout_2.addWidget(self.lblDeckSize)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(OpponentInfo)
        QtCore.QMetaObject.connectSlotsByName(OpponentInfo)

    def retranslateUi(self, OpponentInfo):
        OpponentInfo.setWindowTitle(_translate("OpponentInfo", "Form", None))
        self.lblLifeLabel.setText(_translate("OpponentInfo", "Life:", None))
        self.lblPoisonLabel.setText(_translate("OpponentInfo", "Poison:", None))
        self.lblHandSizeLabel.setText(_translate("OpponentInfo", "Hand Size:", None))
        self.lblDeckSizeLabel.setText(_translate("OpponentInfo", "Deck Size:", None))
        self.lblLife.setText(_translate("OpponentInfo", "20", None))
        self.lblPoison.setText(_translate("OpponentInfo", "0", None))
        self.lblHandSize.setText(_translate("OpponentInfo", "0", None))
        self.lblDeckSize.setText(_translate("OpponentInfo", "0", None))

