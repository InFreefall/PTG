'''
Created on Jul 19, 2011

@author: mitchell
'''

from UI.UI_deckEditor import Ui_DeckEditor
from PyQt4.QtGui import QDialog

class QDeckEditor(QDialog, Ui_DeckEditor):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

if __name__ is '__main__':
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    d = QDeckEditor()
    d.show()
    d.raise_()
    app.exec_()
