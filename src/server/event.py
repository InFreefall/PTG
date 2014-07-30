import Pyro.core

# Type: addPlayer
# data:
#   0: playerID
#   1: playerName

# Type: removePlayer
# data:
#   None - sender tells all

# Type: setDeck
# data:
#   0: deckName
#   1: deckSize

# Type: moveCard
# data:
#   0: abbreviation
#   1: index
#   2: originalPosition
#   3: newPosition
#   4: tapped

# Type: setLife
# data:
#   0: life

# Type: updateSide
# data:
#   0: creatureScroller  format: abbreviation,index abbreviation,index ...
#   1: landScroller
#   2: graveyard
#   3: deckSize

# Type: pleaseUpdate
# data:
#   None - server sends

class Event:#(Pyro.core.ObjBase):
    def __init__(self):
        #Pyro.core.ObjBase.__init__(self)
        self.index = -1
        self.type = ""
        self.data = []
        self.sender = -1
    
    def __description__(self):
        return self.type + " " + str(self.data)
    
    