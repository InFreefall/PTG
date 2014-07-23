import os
import sys
from statedb import Database

database = Database('yugioh.sqlite3')

database.serverInit()
print "Input expansion: "
abbreviation = raw_input()
card_name = ''
while not card_name == 'done':
    print "\nEnter card name (or 'done'): "
    card_name = raw_input()
    if card_name == 'done':
        break
    print '\nEnter card index: '
    index = raw_input()
    database.addCard(index,card_name,'','','','','/%s/%s.jpg'%(abbreviation,index))
