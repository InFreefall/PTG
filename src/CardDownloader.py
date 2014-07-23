'''
Created on Jul 7, 2011

@author: mitchell
'''

import sys
sys.path.append('src')

import cardCrawler
import settingsManager
import statedb
import os
import platform
import ctypes

def main():
    #print "This operation will use approximately %s MB of disk space (not counting cards already downloaded)." % (1.3*1024)
    #print "You have %s MB available." % (get_free_space())
    #print "Continue? (y/n)",
    #input = raw_input()
    #if not input == "y":
    #    print "Canceling..."
    #    return
    
    db = statedb.Database()
    
    db.c.execute('select localFileURL from cards')
    for card in db.c.fetchall():
        localFileURL = card[0]
        parts = localFileURL.split('/')
        abbreviation = parts[-2]
        index = parts[-1].split('.')[0]
        if (os.path.isfile(os.path.join(settingsManager.settings['cardsDir'], abbreviation, '%s.jpg' % (index)))):
            print "%s,%s exists" % (abbreviation, index)
        else:
            print "%s,%s doesnt exist... crawling" % (abbreviation, index)
            cardCrawler.crawlCardAndInfo(abbreviation, index, addToDB=False)

def get_free_space():
    folder = settingsManager.settings['cardsDir']
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        retVal = free_bytes.value
    else:
        retVal = os.statvfs(folder).f_bfree * os.statvfs(folder).f_bsize
    return retVal / (1024 * 1024) # In MB

if __name__ == "__main__":
    main()