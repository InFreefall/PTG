import Networking.GLclient
import random
import statedb
import time
from util import utilities
from Networking.DraftClient import DraftClient
from PyQt4.QtCore import QObject

ALL_COLORS = ['W','B','U','R','G']
random.shuffle(ALL_COLORS)

colors = ALL_COLORS[0:int(random.random()*2) + 2]
print "Picking from colors %s" % colors

def costMatchesColors(cost):
    for color in colors:
        if color in cost:
            return True
    return False

db = statedb.Database()

started=False

class Delegate(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.started=False
    def startGame(self):
        self.started=True
        print "Game started"
    def __getattr__(self, name):
        def method(*args):
            print("tried to handle unknown method " + name)
            if args:
                print("it had arguments: " + str(args))
        return method
delegate = Delegate()

glClient = Networking.GLclient.Client(delegate)
glClient.register("DraftBot")

game = glClient.getGames()[-1]
glClient.joinGame(game)
glClient.registerListenerForGame(delegate,game)

while not delegate.started:
    glClient.eventLoop()
    time.sleep(.25)

game = [g for g in glClient.getGames() if g.gameID == game.gameID][0]
client = DraftClient()
client.setUp(game.gameID, len(game.players), game.expansions)
client.register("DraftBot")
client.signalReady()
while not client.everyoneReady():
    time.sleep(.25)
pack = client.getCurrentPack()
while pack is not ['land']:
    if 'wait' in pack:
        time.sleep(.25)
        continue
    colorCardTuples = [(x,db.manaCostForCard(db.nameForAbbreviationIndex(x[0],x[1]))) for x in pack]
    colorMatches = [x for x in colorCardTuples if costMatchesColors(x[1])]
    card = random.choice(colorMatches)[0]
    client.pickCard(card)
    pack = client.getCurrentPack()
print "Done!"
