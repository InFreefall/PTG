import sqlite3

def cardExp(card):
    try:
        return card[0].split('/')[-2]
    except:
        return "Unknown"

# conn = sqlite3.connect("statedb.sqlite3")
# c = conn.cursor()
# expSet = frozenset([cardExp(card) for card in c.execute('select localFileURL from cards')])
# print str(list(expSet)).replace('u','')

import cardCrawler; cardCrawler.crawlSets()
    
exps = ['gp', 'zen', 'roe', 'ala', 'lg', 'le', 'fve', 'fvd', 'tr', 'ts', 'tp', 'lw', 'pch', '5e', 'fvr', 'dm', 'dk', 'di', '9e', 'ds', 'pc2', 'cmd', 'eve', 'evg', 'dpa', 'shm', '10e', 'arb', 'arc', 'ex', 'cfx', 'tsts', 'wwk', 'gvl', 'pd2', 'st2k', 'ddg', 'ddf', 'bd', 'wl', 'mgbc', '9eb', '8e', 'gtc', 'br', 'on', 'od', 'pds', 'bok', 'dka', 'isd', 'ch', 'sok', 'som', 'm11', 'm10', 'm13', 'm12', 'cs', '5dn', 'mbs', 'pr', 'ps', 'chk', 'pc', '6e', 'jvc', 'hl', 'rav', 'ft', 'mm', 'mi', 'pvc', 'mt', 'mr', '7e', 'ai', 'vi', 'avr', 'an', 'aq', 'ap', 'at', 'in', 'ia', 'haa', 'ne', 'nph', '8eb', 'cstd', 'fe', 'dvd', 'st', 'sh', 'sc', '4e', 'fut', 'ju', 'us', 'uhaa', 'ud', 'ug', 'ul', 'uh']
