# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadScreen.ui'
#
# Created: Wed Feb 27 18:52:57 2013
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

class Ui_loadScreen(object):
    def setupUi(self, loadScreen):
        loadScreen.setObjectName(_fromUtf8("loadScreen"))
        loadScreen.setWindowModality(QtCore.Qt.ApplicationModal)
        loadScreen.resize(400, 69)
        self.infoLabel = QtGui.QLabel(loadScreen)
        self.infoLabel.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.progressBar = QtGui.QProgressBar(loadScreen)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 371, 23))
        self.progressBar.setProperty("value", 23)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(loadScreen)
        QtCore.QMetaObject.connectSlotsByName(loadScreen)

    def retranslateUi(self, loadScreen):
        loadScreen.setWindowTitle(_translate("loadScreen", "Loading", None))
        self.infoLabel.setText(_translate("loadScreen", "Reticulating Splines...", None))

