"""This is a module to download all the card data used by Plamann: The Gathering."""

import urllib2
import urllib
import os
import sys
from BeautifulSoup import BeautifulSoup
import settingsManager
import statedb
import time
import re

import pdb
from util import utilities

def crawlSets():
    statedb.commonDB().serverInit()
    abbreviations = utilities.allExpansions
    i = 0
    for abbreviation in abbreviations:
        i+=1
        print "Crawling set %d of %d" % (i,len(abbreviations))
        crawlSet(abbreviation, False)

def crawlSet(abbreviation, downloadScan=True):
    """This will find all card for a set and send them to another function to download the card.

    A set will be represented by an abbreviation such as "m11\" """

    # Make the folders to hold the card images
    try:
        os.makedirs(os.path.join(settingsManager.settings['cardsDir'],abbreviation))
    except Exception:
        pass # Directory already exists
    url = "http://magiccards.info/%s/en.html" % (abbreviation)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    # Loop through all <tr>s that have a class of "odd" or "even"
    for card in soup.findAll("tr", {"class" : ["odd", "even"]}):
        crawlCard(abbreviation, card, downloadScan=downloadScan)
    statedb.commonDB().commit()

def crawlCardName(cardName):
    """For you crazy people building a deck without an abbreviation and index to go by"""
    cardName = cardName.replace(" ", "+")
    url = "http://magiccards.info/query?q=%s%s" % ('%21', cardName)  # remove spaces from cardName
    page = urllib2.urlopen(url).read()
    regex = '<span style="font-size: 1.5em;">.*?<a href="/(.*?)/en/(.*?).html">.*?<img src="http://magiccards.info/images/en.gif" alt="English"'
    searchResults = re.compile(regex, re.MULTILINE | re.DOTALL).search(page)
    crawlCardAndInfo(searchResults.group(1), searchResults.group(2))

def crawlCardAndInfo(abbreviation, index, addToDB=True, silent=False):
    """
    This function is for calling from within card.py
    It downloads the td row containing the card to download, and passes that to crawlCard
    """
    try:
        os.makedirs(os.path.join(settingsManager.settings['cardsDir'],abbreviation))
    except Exception:
        pass
    if abbreviation.startswith('ygo'):
        crawlYuGiOhCard(abbreviation, index)
        return
    url = "http://magiccards.info/%s/en.html" % (abbreviation)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    print "Downloading (%s,%s)" % (abbreviation, index)
    for card in soup.findAll("tr", {"class" : ["odd", "even"]}):
        if card.find("td", {"align":"right"}).contents[0] == "%s" % (index) \
           or card.find("td", {"align":"right"}).contents[0] == "%sa" % (index):
            crawlCard(abbreviation, card, addToDB, silent=silent)
    if addToDB:
        statedb.commonDB().commit()

def getTRFromAbbreviationIndex(abbreviation, index):
    if abbreviation.startswith('ygo'):
        raise Exception("Yu-Gi-Oh Unimplemented.")
    url = "http://magiccards.info/%s/en.html" % (abbreviation)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    return filter(lambda card: card.find("td", {"align":"right"}).contents[0] == "%s" % (index),soup.findAll("tr", {"class" : ["odd", "even"]}))[0]

def cardInfoFromTrTag(trTag):
    listOfTDs = trTag.findAll("td")
    index = ''
    subIndex = '' # For flip cards. Innistrad makes this unnecessarily difficult.
    workingIndex = listOfTDs[0].contents[0]
    try:
        index = int(workingIndex)
    except: # Can't make an int -- workingIndex must be 23a or 42b or something
        index = int(listOfTDs[0].contents[0][:-1])  # Strip out the letter at the end
        subIndex = listOfTDs[0].contents[0][-1]
        if (subIndex == 'a'):
            pass
        elif (subIndex == 'b'):
            index *= 1000 # Convention I'm using to signify the other side of a flip card
        else:
            raise Exception("Unknown card index: " + workingIndex)
    cardNameTag = trTag.find("a", href=re.compile("/*?/en/%s.html" % (workingIndex)))
    cardName = cardNameTag.contents[0]
    cardType = listOfTDs[2].contents[0]
    try:
        manaCost = listOfTDs[3].contents[0]
    except:
        manaCost = ""
    rarity = listOfTDs[4].contents[0]
    artist = listOfTDs[5].contents[0]
    return (index,workingIndex,cardName,cardType,manaCost,rarity,artist)


def crawlCard(abbreviation, trTag, addToDB=True, downloadScan=True, silent=False):
    try:
        os.makedirs(os.path.join(settingsManager.settings['cardsDir'],abbreviation))
    except Exception:
        pass
    index,workingIndex,cardName,cardType,manaCost,rarity,artist = cardInfoFromTrTag(trTag)
    scanUrl = "http://magiccards.info/scans/en/%s/%s.jpg" % (abbreviation, workingIndex)
    dualUrl = "http://magiccards.info/scans/en/%s/%sa.jpg" % (abbreviation, workingIndex)
    localFileURL = os.path.join(settingsManager.settings['cardsDir'], abbreviation, '%s.jpg' % (index))
    if (downloadScan):
        try:
            urllib.urlretrieve(scanUrl, localFileURL)
        except:
            print "Could not download card from {}, maybe it is a dual card?".format(scanUrl)
            urllib.urlretrieve(dualUrl, localFileURL)

    if addToDB:
        statedb.commonDB().addCard(index,cardName,cardType,manaCost,rarity,artist,localFileURL)

def crawlYuGiOhCard(abbreviation, index):
    url = "http://maxthelizard.dyndns.org/cards/%s/%s.jpg" % (abbreviation,index)
    localFileURL = os.path.join(settingsManager.settings['cardsDir'],abbreviation,'%s.jpg' % (index))
    urllib.urlretrieve(url,localFileURL)
