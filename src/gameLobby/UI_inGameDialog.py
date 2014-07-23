# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inGameDialog.ui'
#
# Created: Fri Oct 21 19:03:28 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_InGameDialog(object):
    def setupUi(self, InGameDialog):
        InGameDialog.setObjectName(_fromUtf8("InGameDialog"))
        InGameDialog.resize(639, 453)
        self.verticalLayout_3 = QtGui.QVBoxLayout(InGameDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnCancel = QtGui.QPushButton(InGameDialog)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnStartGame = QtGui.QPushButton(InGameDialog)
        self.btnStartGame.setObjectName(_fromUtf8("btnStartGame"))
        self.horizontalLayout.addWidget(self.btnStartGame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(InGameDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.wTwoHeadedGiant = QtGui.QWidget(InGameDialog)
        self.wTwoHeadedGiant.setObjectName(_fromUtf8("wTwoHeadedGiant"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.wTwoHeadedGiant)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.wTwoHeadedGiant)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lvTeam1 = QtGui.QListView(self.wTwoHeadedGiant)
        self.lvTeam1.setObjectName(_fromUtf8("lvTeam1"))
        self.verticalLayout.addWidget(self.lvTeam1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.btnSwitchTeams = QtGui.QPushButton(self.wTwoHeadedGiant)
        self.btnSwitchTeams.setObjectName(_fromUtf8("btnSwitchTeams"))
        self.horizontalLayout_4.addWidget(self.btnSwitchTeams)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.wTwoHeadedGiant)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.lvTeam2 = QtGui.QListView(self.wTwoHeadedGiant)
        self.lvTeam2.setObjectName(_fromUtf8("lvTeam2"))
        self.verticalLayout_2.addWidget(self.lvTeam2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.wTwoHeadedGiant)
        self.lvPlayers = QtGui.QListView(InGameDialog)
        self.lvPlayers.setObjectName(_fromUtf8("lvPlayers"))
        self.verticalLayout_3.addWidget(self.lvPlayers)

        self.retranslateUi(InGameDialog)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), InGameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InGameDialog)

    def retranslateUi(self, InGameDialog):
        InGameDialog.setWindowTitle(QtGui.QApplication.translate("InGameDialog", "GAME NAME HERE – NOT THE SAME NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("InGameDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStartGame.setText(QtGui.QApplication.translate("InGameDialog", "Start Game", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InGameDialog", "Players in game:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("InGameDialog", "Team 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSwitchTeams.setText(QtGui.QApplication.translate("InGameDialog", "Switch Teams", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("InGameDialog", "Team 2:", None, QtGui.QApplication.UnicodeUTF8))

