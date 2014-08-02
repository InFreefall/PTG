from Networking import gameClient
import main
import os
import sys
from easygui import msgbox
from util import utilities
sys.path.append('gen-py')

from PTG import PTG
from PTG.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    gameID = int(sys.argv[1])
except:
    msgbox("You need to start PTG through the game lobby.")
    sys.exit(1)

#if os.name is 'nt':
    #msgbox("Why would anyone ever use Windows?")
    #msgbox("This one's for you, will!")

try:
    transport = TSocket.TSocket('maxthelizard.doesntexist.com', 42142)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = PTG.Client(protocol)
    transport.open()
    print "Server version: ", client.VERSION()
    print "My version: ", utilities.VERSION(), "\n"
except Exception, ex:
    msgbox("Mitchell is probably not running the server.")
    print ex
    sys.exit(1)
if client.VERSION() != utilities.VERSION():
    print "Houston, we have a problem. Version mismatch."
    if os.name is 'nt':
        msgbox("You gotta update the app! Mitchell changed something big, and you won't be able to play until you update it!", ok_button="Yessir!")
        #msgbox("Click the button to update! Right now!", ok_button="Yessir!")
        #sys.path.append('WinUpdate')
        #os.system('update.bat')
    else:
        msgbox("Who are you and why didn't you tell me you aren't running Windows? (Please update)")
        sys.exit(1)
transport.close()
main.main()
