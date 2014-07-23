from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class Server:
    def __init__(self):
        self.started = False
        
    def stop(self):
        self.server.done = True
    
    def run(self, service, port, startingMsg = "Starting server...."):
        processor = service.Processor(self)
        transport = TSocket.TServerSocket(port=port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        
        self.server = TServer.TThreadedServer(processor, transport, tfactory, pfactory, daemon=True)
        print startingMsg
        self.started = True
        self.server.serve()
        print "Quitting"
