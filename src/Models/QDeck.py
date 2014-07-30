'''
Created on Jul 13, 2011

@author: mitchell
'''
from Models.QCard import QCard
from Models.QCardModel import QCardModel
import random
import os
import statedb

basicLand = [('m11',230),('m11',237),('m11',239),('m11',244),('m11',246)]

class QDeck(QCardModel):
    def __init__(self, parent, controllable, preferredCardHeight=170,game="Magic",database=None):
        QCardModel.__init__(self, parent, controllable, preferredCardHeight)
        if database == None:
            if game == 'Magic':
                self.db = statedb.commonDB()
            elif game == 'Yu-Gi-Oh':
                self.db = statedb.commonDB('yugioh.sqlite3')
        else:
            self.db = database
        self.commander = None
        self.game = game

    def shuffle(self):
        # TODO: Notify others using beginMoveRows or somthing
        random.shuffle(self.list)

    def removeCommanderFromDeck(self):
        for card in self.list:
            if self.db.nameForAbbreviationIndex(card.abbreviation, card.index) == self.commander:
                self.removeItem(card)
                return card

    def loadFromFile(self, filename, absolute=False):
        self.name = filename
        if absolute:
            f = open(filename)
        elif self.game == 'Yu-Gi-Oh':
            f = open(os.path.join('src','userdata','ygoDecks',filename))
        else:
            f = open(os.path.join('src','userdata','decks',filename))
        line = f.readline()
        if line.startswith("timeStamp:"):
            line = f.readline()
        lines = []
        while line != "":
            lines.append(line)
            line = f.readline()
        self.loadDeckFromLines(lines)

    def loadDeckFromLines(self, lines):
        for line in lines:
            if line.strip() == '' or line.strip()[0] == '#':
                continue
            if line.strip().startswith("Commander:"):
                self.commander = line.strip()[len("Commander:"):].strip()
                print "Commander is %s" % (self.commander)
                continue
            parts = line.split(' x ')
            cardName = line.rstrip()
            numCards = 1
            if len(parts) is not 1:
                cardName = parts[1].rstrip()
                numCards = parts[0].rstrip()
            parts = cardName.split('/')
            abbreviation = ""
            index = ""
            if len(parts) is not 1 and parts[0] == "cards":
                abbreviation = parts[1]
                index = parts[2]
                self.addItem(QCard(abbreviation,index))
            else:
                try:
                    for i in range(0,int(numCards)):
                        try:
                            abbreviation, index = self.db.findCard(cardName)
                        except:
                            import cardCrawler
                            cardCrawler.crawlCardName(cardName)
                            abbreviation, index = self.db.findCard(cardName)
                        self.addItem(QCard(abbreviation,index))
                except Exception:
                    print "Error: could not load card %s" % (cardName)
                    print "Probably a misspelling or something"
        self.shuffle()

    def drawCard(self):
        if len(self.list) is 0:
            return -1, -1
        card = self.list[-1]
        self.removeItem(card)
        return card.abbreviation, card.index

    def makeBoosterFromAbbreviation(self, abbreviation, land=True):
        # Assume 15 cards:
        #   1  basic land
        #   10 commons
        #   3  uncommons
        #   1  rare (1 in 8 is a mythic rare)

        cards = []
        cardList = self.db.cardListWithAbbreviationRarity(abbreviation, 'Common')
        for i in range(0,10):
            choice = random.choice(cardList)
            cardList.remove(choice)
            cards.append(choice)
        cardList = self.db.cardListWithAbbreviationRarity(abbreviation, 'Uncommon')
        for i in range(0,3):
            choice = random.choice(cardList)
            cardList.remove(choice)
            cards.append(choice)
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

    def randomFromColors(self, colors):
        self.loadDeckFromLines(self.tuplesToNameArray(self.generateDeck(colors)))

    def generateDeck(self, colors, size=60, creatures_to_spells_ratio=.5, numLand = 20):
        if len(colors) is not 1:
            raise Exception("Multicolor decks unimplemented!")
        validCards = set()
        for color in colors:
            validCards = validCards.union( set(self.db.cardListWithQuery("SELECT localFileURL FROM cards WHERE manaCost LIKE ?", ('%'+color+'%',))) )
        cardTuples = [self.db.infoForAbbreviationIndex(c[0],c[1]) for c in validCards]

        def isSpell(cardTuple):
            type = cardTuple[3].lower()
            return "enchantment" in type or "instant" in type or "sorcery" in type

        def isCreature(cardTuple):
            type = cardTuple[3].lower()
            return "creature" in type

        # Returns list of names of cards
        landMap = {'B' : 'Swamp',
                   'W' : 'Plains',
                   'U' : 'Island',
                   'R' : 'Mountain',
                   'G' : 'Forest'}

        deck = []
        landCard = self.db.cardListWithQuery("SELECT localFileURL FROM cards WHERE cardName = ?", (landMap[colors[0]],))
        for i in range(numLand):
            deck.append(self.db.infoForAbbreviationIndex(landCard[0][0],landCard[0][1]))

        numCreatures = (size-numLand)*creatures_to_spells_ratio
        numSpells = (size-numLand)*(1-creatures_to_spells_ratio)

        creatures = filter(isCreature,cardTuples)
        spells = filter(isSpell,cardTuples)

        for i in range(int(numCreatures)):
            deck.append(random.choice(creatures))
        for i in range(int(numSpells)):
            deck.append(random.choice(spells))

        return deck

    def tuplesToNameArray(self, deck):
        return [card[2] for card in deck]
