'''
Created on Jul 9, 2011

@author: mitchell
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class QPictureButton(QPushButton):
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)
        painter = QPainter(self)
        painter.drawPixmap(QRect(QPoint(), self.size()), self.pixmap, self.pixmap.rect())