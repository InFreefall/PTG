from CardRules.CardConstants import *
from CardRules.BaseCardRule import BaseCardRule
 
class Plains(BaseCardRule):
    def __init__(self):
        BaseCardRule.__init__(self)
        self.setName('Plains')
        self.types = [CardType.Land, CardSubtype.Plains]
