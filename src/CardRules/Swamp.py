from CardRules.CardConstants import *
from CardRules.BaseCardRule import BaseCardRule

class Swamp(BaseCardRule):
    def __init__(self):
        BaseCardRule.__init__(self)
        self.types = [CardType.Land,CardSubtype.Swamp]
        self.addActivated(tap=True, action=addManaToPool(B=1))
