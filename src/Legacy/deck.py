import random
import os
from MinimalCard import MinimalCard
from statedb import Database

basicLand = [('m11',230),('m11',237),('m11',239),('m11',244),('m11',246)]

class Deck:
    def __init__(self):
        self.cards = []
        self.db = Database()
    
    def shuffle(self):
        random.shuffle(self.cards)
        print "Deck is shuffled."
    
    def loadFromFile(self, filename, absolute=False):
        self.name = filename
        if absolute:
            file = open(filename)
        else:
            file = open(os.path.join('src','userdata','decks',filename))
        line = file.readline()
        if line.startswith("timeStamp:"):
            line = file.readline()
        while line != "":
            if line.strip() == '' or line.strip()[0] == '#':
                line = file.readline()
                continue
            parts = line.split(' x ')
            cardName = line.rstrip()
            numCards = 1
            if len(parts) is not 1:
                cardName = parts[1].rstrip()
                numCards = parts[0].rstrip()
            parts = cardName.split('/')
            if len(parts) is not 1 and parts[0] == "cards":
                self.cards.append(MinimalCard(parts[1],parts[2]))
            else:
                try:
                    for i in range(0,int(numCards)): #@UnusedVariable
                        try:
                            abbreviation, index = self.db.findCard(cardName)
                        except:
                            import cardCrawler
                            cardCrawler.crawlCardName(cardName)
                            abbreviation, index = self.db.findCard(cardName)
                        self.cards.append(MinimalCard(abbreviation,index))
                except Exception:
                    print "Error: could not load card %s" % (cardName)
                    print "Probably a misspelling or something"
            line = file.readline()
        self.shuffle()
    
    def drawCard(self):
        if len(self.cards) is 0:
            return -1, -1
        card = self.cards.pop()
        return card.abbreviation, card.index
    
    def makeBoosterFromAbbreviation(self, abbreviation, land=True):
        # Assume 15 cards:
        #   1  basic land
        #   10 commons
        #   3  uncommons
        #   1  rare (1 in 8 is a mythic rare)
        
        cards = []
        for i in range(0,10): #@UnusedVariable
            cards.append(random.choice(self.db.cardListWithAbbreviationRarity(abbreviation, 'Common')))
        for i in range(0,3): #@UnusedVariable
            cards.append(random.choice(self.db.cardListWithAbbreviationRarity(abbreviation, 'Uncommon')))
        mythic = False
        if random.randint(0,7) == 0:
            try:
                cards.append(random.choice(self.db.cardListWithAbbreviationRarity(abbreviation, 'Mythic Rare')))
                mythic = True
            except:
                # No mythic rares available in this expansion
                pass
        if mythic == False:
            cards.append(random.choice(self.db.cardListWithAbbreviationRarity(abbreviation, 'Rare')))
        if land:
            try:
                cards.append(random.choice(self.db.cardListWithAbbreviationRarity(abbreviation, 'Land')))
            except:
                cards.append(random.choice(self.db.cardListWithAbbreviationRarity('m11', 'Land')))
                #Basic land is the same in anything, and this abbreviation has no basic land
        return cards