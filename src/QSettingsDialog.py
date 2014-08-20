'''
Created on Jul 25, 2011

@author: mitchell
'''

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL
from UI.UI_settings import Ui_settingsDialog
import settingsManager

class QSettingsDialog(QDialog, Ui_settingsDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connect(self, SIGNAL('accepted()'), self.accepted)
        self.cbAutoSwitch.setChecked(settingsManager.settings['switchOnPlayerMove'])
        self.cbReportCrashes.setChecked(settingsManager.settings['reportCrashes'])
        self.leServerName.setText(settingsManager.settings['hostname'])
        self.leCardsDir.setText(settingsManager.settings['cardsDir'])
    
    def accepted(self):
        settingsManager.settings['switchOnPlayerMove'] = self.cbAutoSwitch.isChecked()
        settingsManager.settings['reportCrashes'] = self.cbReportCrashes.isChecked()
        settingsManager.settings['hostname'] = str(self.leServerName.text())
        settingsManager.settings['cardsDir'] = str(self.leCardsDir.text())
        settingsManager.save()
