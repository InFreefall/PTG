'''
Created on Jun 29, 2011

@author: mitchell
'''
import os
import pickle

SETTINGS_FILE = ""
try:
    SETTINGS_FILE = os.path.join(os.environ['HOME'],'.ptg','PTG.settings')
except:
    pass
if not os.path.isfile(SETTINGS_FILE):
    SETTINGS_FILE = os.path.join('src','userdata',"PTG.settings")

# Default values
settings = {
            'cardsDir':os.path.join('src','cards'),
            'imagesDir':'images',
            'hasMovedDecks':False,
            'reportCrashes':True,
            'switchOnPlayerMove':True,
            'hostname':'maxthelizard.doesntexist.com',
            'randomize':False
            }
def save():
    with open(SETTINGS_FILE, 'w') as f:
        pass
    with open(SETTINGS_FILE, 'wb') as f:
        pickle.dump(settings, f)

try:
    with open(SETTINGS_FILE, 'rb') as f:
        loadedSettings = pickle.load(f)
        for key in loadedSettings:
            settings[key] = loadedSettings[key]
except IOError:
    #File does not exist
    save()
