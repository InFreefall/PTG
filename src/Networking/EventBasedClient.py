'''
Created on Jun 29, 2011

@author: mitchell
'''

from PyQt4.QtCore import QObject, QTimer, SIGNAL
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol

class EventBasedClient(QObject):

    def __init__(self, clientObject, hostname, port, parentObject, fastForward=False):
        QObject.__init__(self, parentObject)
        self.transport = TSocket.TSocket(hostname, port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = clientObject(self.protocol)
        self.transport.open()
        self.lastEventIndex = -1
        
        self.mappings = {}
        
        self.playerID = -1
        self.playerIDIgnores = []
        self.fastForward = fastForward
    
    def addMapping(self, eventName, function):
        # TODO: Add check if mapping really does exist
        try:
            self.mappings[eventName]
            print "Note: Mapping already exists for event %s, overwriting."
        except KeyError:
            pass
        self.mappings[eventName] = function
    
    def removeMapping(self, eventName):
        try:
            del self.mappings[eventName]
        except:
            pass
    
    def startEventLoop(self, eventFunction):
        '''Be sure to have playerID set. Called separately from the constructor to allow subclasses a chance to change, say, lastEventIndex'''
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL('timeout()'), self.eventLoop)
        self.timer.start(500);
        self.eventFunction = eventFunction
    
    def endEventLoop(self):
        self.timer.stop()
    
    def eventLoop(self):
        events = self.eventFunction(self.lastEventIndex)
        self.lastEventIndex += len(events)
        for event in events:
            if event.sender == self.playerID and event.type not in self.playerIDIgnores and not self.fastForward:
                continue
            try:
                eventListener = self.mappings[event.type]
            except:
                # Mapping does not exist for event.type
                print "Unknown event: " + event.type
            eventListener(event)
        if self.fastForward:
            self.fastForward = False
