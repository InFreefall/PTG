from PyQt4.QtGui import QDialog
from UI.UI_loadScreen import Ui_loadScreen

class QLoadingDialog(QDialog, Ui_loadScreen):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

    def setProgress(self, progress):
        self.progressBar.setValue(progress)

    def setLabel(self, text):
        self.infoLabel.setText(text)
