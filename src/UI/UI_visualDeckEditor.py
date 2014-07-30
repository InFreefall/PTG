# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualDeckEditor.ui'
#
# Created: Tue Jul 29 18:30:32 2014
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

class Ui_visualDeckEditor(object):
    def setupUi(self, visualDeckEditor):
        visualDeckEditor.setObjectName(_fromUtf8("visualDeckEditor"))
        visualDeckEditor.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(visualDeckEditor.sizePolicy().hasHeightForWidth())
        visualDeckEditor.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(visualDeckEditor)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(visualDeckEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabRed = QtGui.QWidget()
        self.tabRed.setObjectName(_fromUtf8("tabRed"))
        self.tabWidget.addTab(self.tabRed, _fromUtf8(""))
        self.tabGreen = QtGui.QWidget()
        self.tabGreen.setObjectName(_fromUtf8("tabGreen"))
        self.tabWidget.addTab(self.tabGreen, _fromUtf8(""))
        self.tabBlue = QtGui.QWidget()
        self.tabBlue.setObjectName(_fromUtf8("tabBlue"))
        self.tabWidget.addTab(self.tabBlue, _fromUtf8(""))
        self.tabWhite = QtGui.QWidget()
        self.tabWhite.setObjectName(_fromUtf8("tabWhite"))
        self.tabWidget.addTab(self.tabWhite, _fromUtf8(""))
        self.tabBlack = QtGui.QWidget()
        self.tabBlack.setObjectName(_fromUtf8("tabBlack"))
        self.tabWidget.addTab(self.tabBlack, _fromUtf8(""))
        self.tabMulticolor = QtGui.QWidget()
        self.tabMulticolor.setObjectName(_fromUtf8("tabMulticolor"))
        self.tabWidget.addTab(self.tabMulticolor, _fromUtf8(""))
        self.tabColorless = QtGui.QWidget()
        self.tabColorless.setObjectName(_fromUtf8("tabColorless"))
        self.tabWidget.addTab(self.tabColorless, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(visualDeckEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(visualDeckEditor)

    def retranslateUi(self, visualDeckEditor):
        visualDeckEditor.setWindowTitle(_translate("visualDeckEditor", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRed), _translate("visualDeckEditor", "Red", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGreen), _translate("visualDeckEditor", "Green", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBlue), _translate("visualDeckEditor", "Blue", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWhite), _translate("visualDeckEditor", "White", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBlack), _translate("visualDeckEditor", "Black", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMulticolor), _translate("visualDeckEditor", "Multicolor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabColorless), _translate("visualDeckEditor", "Colorless", None))

