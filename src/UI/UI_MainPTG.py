# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPTG.ui'
#
# Created: Thu May 30 01:05:03 2013
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

class Ui_MainPTG(object):
    def setupUi(self, MainPTG):
        MainPTG.setObjectName(_fromUtf8("MainPTG"))
        MainPTG.resize(1267, 825)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(MainPTG)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.twOpponents = QtGui.QTabWidget(MainPTG)
        self.twOpponents.setTabPosition(QtGui.QTabWidget.North)
        self.twOpponents.setObjectName(_fromUtf8("twOpponents"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.twOpponents.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.twOpponents.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.twOpponents)
        self.twTeam = QtGui.QTabWidget(MainPTG)
        self.twTeam.setObjectName(_fromUtf8("twTeam"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.twTeam.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.twTeam.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.twTeam)
        self.lblHand = QtGui.QLabel(MainPTG)
        self.lblHand.setObjectName(_fromUtf8("lblHand"))
        self.verticalLayout_4.addWidget(self.lblHand)
        self.lvHand = QtGui.QListView(MainPTG)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvHand.sizePolicy().hasHeightForWidth())
        self.lvHand.setSizePolicy(sizePolicy)
        self.lvHand.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvHand.setDragEnabled(True)
        self.lvHand.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lvHand.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lvHand.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lvHand.setFlow(QtGui.QListView.LeftToRight)
        self.lvHand.setObjectName(_fromUtf8("lvHand"))
        self.verticalLayout_4.addWidget(self.lvHand)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.sidebarLayout = QtGui.QVBoxLayout()
        self.sidebarLayout.setObjectName(_fromUtf8("sidebarLayout"))
        self.lblSelectedCard = QtGui.QLabel(MainPTG)
        self.lblSelectedCard.setMaximumSize(QtCore.QSize(312, 445))
        self.lblSelectedCard.setText(_fromUtf8(""))
        self.lblSelectedCard.setPixmap(QtGui.QPixmap(_fromUtf8(":/test/images/back.jpg")))
        self.lblSelectedCard.setScaledContents(False)
        self.lblSelectedCard.setObjectName(_fromUtf8("lblSelectedCard"))
        self.sidebarLayout.addWidget(self.lblSelectedCard)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblLife = QtGui.QLabel(MainPTG)
        self.lblLife.setObjectName(_fromUtf8("lblLife"))
        self.horizontalLayout.addWidget(self.lblLife)
        self.sbLife = QtGui.QSpinBox(MainPTG)
        self.sbLife.setMinimum(-1000000)
        self.sbLife.setMaximum(1000000)
        self.sbLife.setProperty("value", 20)
        self.sbLife.setObjectName(_fromUtf8("sbLife"))
        self.horizontalLayout.addWidget(self.sbLife)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lblPoison = QtGui.QLabel(MainPTG)
        self.lblPoison.setObjectName(_fromUtf8("lblPoison"))
        self.horizontalLayout_2.addWidget(self.lblPoison)
        self.sbPoison = QtGui.QSpinBox(MainPTG)
        self.sbPoison.setObjectName(_fromUtf8("sbPoison"))
        self.horizontalLayout_2.addWidget(self.sbPoison)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sidebarLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem4)
        self.btnViewExile = QtGui.QPushButton(MainPTG)
        self.btnViewExile.setObjectName(_fromUtf8("btnViewExile"))
        self.sidebarLayout.addWidget(self.btnViewExile)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnAddToken = QtGui.QPushButton(MainPTG)
        self.btnAddToken.setObjectName(_fromUtf8("btnAddToken"))
        self.horizontalLayout_3.addWidget(self.btnAddToken)
        self.btnUntapAll = QtGui.QPushButton(MainPTG)
        self.btnUntapAll.setObjectName(_fromUtf8("btnUntapAll"))
        self.horizontalLayout_3.addWidget(self.btnUntapAll)
        self.sidebarLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.sidebarLayout)

        self.retranslateUi(MainPTG)
        self.twOpponents.setCurrentIndex(1)
        self.twTeam.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainPTG)

    def retranslateUi(self, MainPTG):
        MainPTG.setWindowTitle(_translate("MainPTG", "Plamann: The Gathering", None))
        self.twOpponents.setTabText(self.twOpponents.indexOf(self.tab), _translate("MainPTG", "Ozymandius", None))
        self.twOpponents.setTabText(self.twOpponents.indexOf(self.tab_2), _translate("MainPTG", "Bubbers", None))
        self.twTeam.setTabText(self.twTeam.indexOf(self.tab_3), _translate("MainPTG", "I HAVE FAWFUL", None))
        self.twTeam.setTabText(self.twTeam.indexOf(self.tab_4), _translate("MainPTG", "Will", None))
        self.lblHand.setText(_translate("MainPTG", "Your Hand (0 Cards):", None))
        self.lblLife.setText(_translate("MainPTG", "Life:", None))
        self.lblPoison.setText(_translate("MainPTG", "Poison:", None))
        self.btnViewExile.setText(_translate("MainPTG", "View Exile", None))
        self.btnAddToken.setText(_translate("MainPTG", "Add Token", None))
        self.btnUntapAll.setText(_translate("MainPTG", "Untap All", None))

