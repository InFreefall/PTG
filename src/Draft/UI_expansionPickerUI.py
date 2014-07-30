# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expansionPicker.ui'
#
# Created: Fri Oct 21 19:03:29 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExpansionPicker(object):
    def setupUi(self, ExpansionPicker):
        ExpansionPicker.setObjectName(_fromUtf8("ExpansionPicker"))
        ExpansionPicker.resize(684, 481)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ExpansionPicker)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lvAvailable = QtGui.QListView(ExpansionPicker)
        self.lvAvailable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lvAvailable.setObjectName(_fromUtf8("lvAvailable"))
        self.horizontalLayout.addWidget(self.lvAvailable)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnAdd = QtGui.QPushButton(ExpansionPicker)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QPushButton(ExpansionPicker)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.verticalLayout.addWidget(self.btnRemove)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lvSelected = QtGui.QListView(ExpansionPicker)
        self.lvSelected.setObjectName(_fromUtf8("lvSelected"))
        self.horizontalLayout.addWidget(self.lvSelected)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnOK = QtGui.QPushButton(ExpansionPicker)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.horizontalLayout_2.addWidget(self.btnOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ExpansionPicker)
        QtCore.QMetaObject.connectSlotsByName(ExpansionPicker)

    def retranslateUi(self, ExpansionPicker):
        ExpansionPicker.setWindowTitle(QtGui.QApplication.translate("ExpansionPicker", "Pick Your Expansions", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("ExpansionPicker", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setText(QtGui.QApplication.translate("ExpansionPicker", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOK.setText(QtGui.QApplication.translate("ExpansionPicker", "OK", None, QtGui.QApplication.UnicodeUTF8))

