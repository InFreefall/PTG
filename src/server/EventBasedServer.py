from Server import Server

class EventBasedServer(Server):
    def __init__(self):
        Server.__init__(self)
        self.events = []
        self.additionalHandlers = {}
    
    def addHandler(self, eventType, handler):
        self.additionalHandlers[eventType] = handler
    
    def addEvent(self, event):
        handler = None
        try:
            handler = self.additionalHandlers[event.type]
        except:
            pass
        if handler is not None:
            handler(event)
        try:
            event.senderName = self.players[event.sender].playerName
        except:
            pass
        self.events.append(event)
        event.index = self.events.index(event)
    
    def currentEventIndex(self):
        return len(self.events)-1
    
    def getEvents(self, sinceIndex):
        retVal = self.events[(sinceIndex+1):]
        return retVal