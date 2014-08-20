'''
Created on Aug 22, 2011

@author: mitchell
'''

from PyQt4.QtGui import QWidget, QListView, QAbstractItemView, QVBoxLayout, QLabel, QPushButton
from PyQt4.QtCore import SIGNAL, QSize
from util import utilities

class QCardListViewer(QWidget):
    def __init__(self, model, enlargeFunction, parent):
        QWidget.__init__(self, parent)
        
        def enlarge(index):
            enlargeFunction(model.list[index.row()])
        
        windowSize = self.window().frameSize()
        self.resize(QSize(windowSize.width()-(25+utilities.bigCardSize[0]),275))
        
        lvViewer = QListView(self)
        lvViewer.setModel(model)
        lvViewer.setDragEnabled(True)
        lvViewer.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        lvViewer.setFlow(QListView.LeftToRight)
        lvViewer.setFocus()
        self.connect(lvViewer, SIGNAL('clicked(QModelIndex)'), enlarge)
        
        button = QPushButton("Close", self)
        self.connect(button,SIGNAL('clicked()'),self.hide)
        
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("I'm sorry this is so ugly.",self))
        layout.addWidget(lvViewer)
        layout.addWidget(button)
        self.setLayout(layout)
        
        self.show()