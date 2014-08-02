from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

events = []
additionalHandlers = {}

@dispatcher.add_method
def addEvent(**kwargs):
    event = kwargs['event']
    handler = None
    try:
        handler = additionalHandlers[event['type']]
    except:
        pass
    if handler is not None:
        handler(event)
    try:
        event['senderName'] = players[event['sender']].playerName
    except:
        pass
    events.append(event)
    event['index'] = events.index(event)

@dispatcher.add_method
def currentEventIndex():
    return len(events)-1

@dispatcher.add_method
def getEvents(sinceIndex):
    return events[(sinceIndex+1):]
    
@Request.application
def application(request):
    dispatcher['addEvent'] = addEvent
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)
