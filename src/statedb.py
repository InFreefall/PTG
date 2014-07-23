import sqlite3
import random
import os
import threading
import settingsManager

def commonDB(filename='statedb.sqlite3'):
    if commonDB.instance is None:
        commonDB.instance = {}
    try:
        return commonDB.instance[filename]
    except KeyError:
        commonDB.instance[filename] = Database(filename)
        return commonDB.instance[filename]
commonDB.instance = {}

def closeDB():
    commonDB.instance = None

class CardLookupException(Exception):
    pass

class Database:
    def __init__(self,filename='statedb.sqlite3'):
        self.conn = sqlite3.connect(os.path.join('src',filename))
        self.c = self.conn.cursor()

    def serverInit(self):
        """This function sets up the table containing the card data.

        It is only meant to be called via cardCrawler"""

        self.c.execute('''create table if not exists cards (cardIndex integer, cardName text, cardType text, manaCost text, rarity text, artist text, localFileURL text)''')
        self.conn.commit()
        print "server database initialized"

    def addCard(self, index, cardName, cardType, manaCost, rarity, artist, localFileURL):
        t = (index, cardName, cardType, manaCost, rarity, artist, localFileURL)
        self.c.execute('insert into cards values (?, ?, ?, ?, ?, ?, ?)', t)
        self.commit()

    def findCard(self, cardName):
        # localFileURL is cards/abbreviation/index.jpg
        self.c.execute('select localFileURL from cards where cardName = ?', (cardName,))
        localFiles = self.c.fetchall()
        try:
            if settingsManager.settings['randomize']:
                localFileURL = random.choice(localFiles)[0]
            else:
                localFileURL = localFiles[0][0]
        except IndexError:
            raise CardLookupException("Could not find card with name %s" % (cardName))
        localFileURL = localFileURL.replace('\\','/')
        parts = localFileURL.split('/')
        return parts[-2], parts[-1].split('.')[0] # Abbreviation, index

    def nameForAbbreviationIndex(self, abbreviation, index):
        self.c.execute('select cardName from cards where localFileURL LIKE ?', ('%'+abbreviation+'/'+str(index)+'%',))
        name = self.c.fetchone()
        return name[0]

    def infoForAbbreviationIndex(self, abbreviation, index):
        self.c.execute('select cardName, cardType, manaCost, rarity, artist from cards where localFileURL like ?', ('%'+abbreviation+'/'+str(index)+'%',))
        return (abbreviation, index) + self.c.fetchone()

    def manaCostForCard(self, cardName):
        self.c.execute('select manaCost from cards where cardName = ?', (cardName,))
        localFiles = self.c.fetchall()
        try:
            return random.choice(localFiles)[0]
        except IndexError:
            raise CardLookupException("Could not find card with name %s" % (cardName))


    def cardListWithAbbreviationRarity(self, abbreviation, rarity):
        return self.cardListWithQuery('select localFileURL from cards where localFileURL LIKE ? and rarity = ?', ('%/'+abbreviation+'/%', rarity))

    def cardListWithQuery(self, qString, args):
        self.c.execute(qString, args)
        unmodifiedCardURLs = self.c.fetchall()
        cardURLs = [(card[0].replace('\\','/'),) for card in unmodifiedCardURLs]
        return [(card[0].split('/')[-2],card[0].split('/')[-1].split('.')[0]) for card in cardURLs]

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.c.close()
