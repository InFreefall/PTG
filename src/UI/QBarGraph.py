'''
Created on Aug 21, 2011

@author: mitchell
'''

from PyQt4.QtGui import QGraphicsView, QGraphicsRectItem, QPainter, QApplication, QGraphicsScene, QBrush, QColor
from PyQt4.QtCore import QSize
import sys

PADDING = 30
BAR_WIDTH = 30
BAR_PADDING = 7
SCENE_HEIGHT = 300.0

class QBarGraph(QGraphicsView):
    def __init__(self, *args):
        scene = QGraphicsScene(args[0])
        scene.setSceneRect(0,0,600.0,SCENE_HEIGHT)
        QGraphicsView.__init__(self, scene, *args)
        
        scene = self.scene()
        self.yAxis = scene.addLine(PADDING, PADDING, PADDING, scene.height() - PADDING)
        self.xAxis = scene.addLine(PADDING, scene.height() - PADDING, scene.width() - PADDING, scene.height() - PADDING)
        
        self.bars = []
        self.barLabels = []
        self.xLabels = []
        self.yLabels = []
        self.values = []
        
        self.show()
        self.raise_()
    
    def resizeEvent(self, event):
        self.setValues(self.values)
    
    def setValues(self, values):
        self.values = values
        scene = self.scene()
        
        for array in (self.barLabels, self.bars, self.xLabels, self.yLabels, [self.xAxis, self.yAxis]):
            for item in array:
                itemScene = item.scene()
                if itemScene is not None:
                    itemScene.removeItem(item)
        
        self.yAxis = scene.addLine(PADDING, PADDING, PADDING, scene.height() - PADDING)
        self.xAxis = scene.addLine(PADDING, scene.height() - PADDING, scene.width() - PADDING, scene.height() - PADDING)
        
        greatestValue = 1
        for value in values:
            if value > greatestValue:
                greatestValue = value
        scale = float(scene.height() - 2 * PADDING) / float(greatestValue)
        curX = PADDING + 5
        h = scene.height()
        for i,value in enumerate(values):
            bottomLine = h - PADDING
            top = h - PADDING - (value*scale)
            
            bar = scene.addRect(curX, top, BAR_WIDTH, bottomLine - top) 
            bar.setBrush(QBrush(QColor("blue")))
            self.bars.append(bar)
            
            if i + 1 == len(values):
                xLabel = scene.addText("X")
            else:
                xLabel = scene.addText("%d" % (i))
            xLabel.setPos(curX + BAR_WIDTH / 2 - xLabel.boundingRect().width() /2, h - xLabel.boundingRect().height())
            self.xLabels.append(xLabel)
            
            barLabel = scene.addText("%d" % (value))
            barLabel.setPos(curX + BAR_WIDTH / 2 - barLabel.boundingRect().width()/2, h - (bottomLine - top) - PADDING - barLabel.boundingRect().height())
            self.barLabels.append(barLabel)
            
            curX += BAR_WIDTH + BAR_PADDING
        
        scene.setSceneRect(0,0,curX + PADDING, SCENE_HEIGHT)
        self.updateGeometry()
    
    def sizeHint(self):
        #import pdb; pdb.set_trace()
        size = self.sceneRect().size()
        return QSize(int(size.width()), int(size.height() + PADDING))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    scene.setSceneRect(0,0,500.0,500.0)
    window = QBarGraph()
    window.setValues([50,20,75,205, 15, 400, 6000])
    result = app.exec_()
    sys.exit(result)