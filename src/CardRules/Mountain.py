from CardRules.CardConstants import *
from CardRules.BaseCardRule import BaseCardRule
 
class Mountain(BaseCardRule):
    def __init__(self):
        BaseCardRule.__init__(self)
        self.setName('Mountain')
        self.types = [CardType.Land, CardSubtype.Mountain]
