# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameLobby.ui'
#
# Created: Fri Oct 21 19:03:27 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnCreateGame = QtGui.QPushButton(self.centralwidget)
        self.btnCreateGame.setObjectName(_fromUtf8("btnCreateGame"))
        self.horizontalLayout.addWidget(self.btnCreateGame)
        self.btnJoinGame = QtGui.QPushButton(self.centralwidget)
        self.btnJoinGame.setObjectName(_fromUtf8("btnJoinGame"))
        self.horizontalLayout.addWidget(self.btnJoinGame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lvGames = QtGui.QListView(self.centralwidget)
        self.lvGames.setObjectName(_fromUtf8("lvGames"))
        self.verticalLayout.addWidget(self.lvGames)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.lvPlayers = QtGui.QListView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvPlayers.sizePolicy().hasHeightForWidth())
        self.lvPlayers.setSizePolicy(sizePolicy)
        self.lvPlayers.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.lvPlayers.setObjectName(_fromUtf8("lvPlayers"))
        self.verticalLayout_2.addWidget(self.lvPlayers)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PTG Game Lobby", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreateGame.setText(QtGui.QApplication.translate("MainWindow", "Create New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.btnJoinGame.setText(QtGui.QApplication.translate("MainWindow", "Join Game", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Games:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Players:", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))

