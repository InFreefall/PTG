'''
Created on Jul 9, 2011

@author: mitchell
'''
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost",8000), requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(pow)

class simple:
    def __init__(self):
        self.x = -1
        self.y = 3

def make():
    return simple() # Works - easy

server.register_function(make)

server.serve_forever()