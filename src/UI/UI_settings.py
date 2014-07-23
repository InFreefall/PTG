# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(455, 407)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbAutoSwitch = QtGui.QCheckBox(settingsDialog)
        self.cbAutoSwitch.setObjectName(_fromUtf8("cbAutoSwitch"))
        self.verticalLayout.addWidget(self.cbAutoSwitch)
        self.cbReportCrashes = QtGui.QCheckBox(settingsDialog)
        self.cbReportCrashes.setObjectName(_fromUtf8("cbReportCrashes"))
        self.verticalLayout.addWidget(self.cbReportCrashes)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(settingsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.leServerName = QtGui.QLineEdit(settingsDialog)
        self.leServerName.setObjectName(_fromUtf8("leServerName"))
        self.horizontalLayout.addWidget(self.leServerName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(settingsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leCardsDir = QtGui.QLineEdit(settingsDialog)
        self.leCardsDir.setObjectName(_fromUtf8("leCardsDir"))
        self.horizontalLayout_2.addWidget(self.leCardsDir)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog", None))
        self.cbAutoSwitch.setText(_translate("settingsDialog", "Automatically switch tabs when a player plays a card", None))
        self.cbReportCrashes.setText(_translate("settingsDialog", "Report crashes to help with development", None))
        self.label.setText(_translate("settingsDialog", "Server Name:", None))
        self.label_2.setText(_translate("settingsDialog", "Cards Directory:", None))

