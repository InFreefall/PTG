import statedb
import json
import os
import settingsManager
import urllib

def tryGet(card, val):
    try:
        return card[val]
    except:
        return ""

def crawlJSON(filename):
    with open(filename) as f:
        mtgSet = json.loads(f.read())

        db = statedb.Database()

        for card in mtgSet['cards']:
            localFileURL = os.path.join(settingsManager.settings['cardsDir'],
                                        mtgSet['code'],
                                        '%s.png' % (card['number']))
            
            # db.addCard(tryGet(card,'number'), tryGet(card,'name'), tryGet(card,'type'),
            #            tryGet(card,'manaCost'), tryGet(card,'rarity'), tryGet(card,'artist'),
            #            localFileURL)
            urllib.urlretrieve("http://mtgimage.com/multiverseid/{}.jpg".format(card['multiverseid']), localFileURL)
        db.commit()

        
