class Util:
    smallCardSize = (135,193)
    smallCardSizeTapped = (193, 135)
    bigCardSize = (312, 445)
    setContextMenu = "setContextMenu"
    allExpansions = ['m14', 'gp', 'zen', 'roe', 'ala', 'lg', 'le', 'fve', 'fvd', 'tr', 'ts', 'tp', 'lw', 'pch', '5e', 'fvr', 'dm', 'dk', 'di', '9e', 'ds', 'pc2', 'cmd', 'eve', 'evg', 'dpa', 'shm', '10e', 'arb', 'arc', 'ex', 'cfx', 'tsts', 'wwk', 'gvl', 'pd2', 'st2k', 'ddg', 'ddf', 'bd', 'wl', 'mgbc', '9eb', '8e', 'gtc', 'br', 'on', 'od', 'pds', 'bok', 'dka', 'isd', 'ch', 'sok', 'som', 'm11', 'm10', 'm13', 'm12', 'cs', '5dn', 'mbs', 'pr', 'ps', 'chk', 'pc', '6e', 'jvc', 'hl', 'rav', 'ft', 'mm', 'mi', 'pvc', 'mt', 'mr', '7e', 'ai', 'vi', 'avr', 'an', 'aq', 'ap', 'at', 'in', 'ia', 'haa', 'ne', 'nph', '8eb', 'cstd', 'fe', 'dvd', 'st', 'sh', 'sc', '4e', 'fut', 'ju', 'us', 'uhaa', 'ud', 'ug', 'ul', 'uh', 'rtr', 'dgm']
    expansionDict = {'gp': 'Guildpact', 'zen': 'Zendikar', 'ala': 'Shards of Alara', 'roe': 'Rise of the Eldrazi', 'lg': 'Legends', 'le': 'Legions', 'fve': 'From the Vault: Exiled', 'fvd': 'From the Vault: Dragons', 'tr': 'Torment', 'ts': 'Time Spiral', 'tp': 'Tempest', 'lw': 'Lorwyn', 'pch': 'Planechase', '5e': 'Fifth Edition', 'fvr': 'From the Vault: Relics', 'dm': 'Deckmasters', 'dk': 'The Dark', 'di': 'Disension', '9e': 'Ninth Edition', 'ds': 'Darksteel', 'cmd': 'Commander', 'eve': 'Eventide', 'evg': 'Duel Decks: Elves vs. Goblins', 'dpa': 'Duels of the Planeswalkers', 'shm': 'Shadowmoor', '10e': 'Tenth Edition', 'arb': 'Alara Reborn', 'arc': 'Archenemy', 'ex': 'Exodus', 'cfx': 'Conflux', 'tsts': 'Time Spiral "Timeshifted"', 'wwk': 'Worldwake', 'rv': 'Revised Edition', 'gvl': 'Duel Decks: Garruk vs. Liliana', 'ul': "Urza's Legacy", 'pd2': 'Premium Deck Series: Fire and Lightning', 'ddg': 'Duel Decks: Knights vs. Dragons', 'ddf': 'Duel Decks: Elspeth vs. Tezzeret', 'bd': 'Beatdown Box Set', 'be': 'Limited Edition Beta', '9eb': 'Ninth Edition Box Set', 'mgbc': 'Multiverse Gift Box Cards', 'ju': 'Judgment', 'wl': 'Weatherlight', '8e': 'Eighth Edition', 'br': 'Battle Royale Box Set', 'on': 'Onslaught', 'od': 'Odyssey', 'pds': 'Premium Deck Series: Slivers', 'bok': 'Betrayers of Kamigawa', 'ch': 'Chronicles', 'sok': 'Saviors of Kamigawa', 'som': 'Scars of Mirrodin', 'm11': 'Magic 2011', 'm10': 'Magic 2010', 'm12': 'Magic 2012', 'cs': 'Coldsnap', '5dn': 'Fifth Dawn', 'mbs': 'Mirrodin Besieged', 'pr': 'Prophecy', 'ps': 'Planeshift', 'chk': 'Champions of Kamigawa', 'pc': 'Planar Chaos', '6e': 'Sixth Edition', 'jvc': 'Duel Decks: Jace vs. Chandra', 'hl': 'Homelands', 'rav': 'Ravnica: City of Guilds', 'fut': 'Future Sight', 'mm': 'Mercadian Masques', 'mi': 'Mirrodin', 'pvc': 'Duel Decks: Phyrexia vs. The Coalition', 'us': "Urza's Saga", 'mt': 'Morningtide', 'un': 'Unlimited Edition', 'uh': 'Unhinged', 'mr': 'Mirage', 'ud': "Urza's Destiny", 'ug': 'Unglued', '7e': 'Seventh Edition', 'ai': 'Alliances', 'vi': 'Visions', 'al': 'Limited Edition Alpha', 'an': 'Arabian Nights', 'aq': 'Antiquities', 'ap': 'Apocalypse', 'at': 'Anthologies', 'in': 'Invasion', 'ia': 'Ice Age', 'uhaa': 'Unhinged Alternate Foils', 'ne': 'Nemesis', 'nph': 'New Phyrexia', '8eb': 'Eighth Edition Box Set', 'cstd': 'Coldsnap Theme Decks', 'fe': 'Fallen Empires', 'dvd': 'Duel Decks: Divine vs. Demonic', 'sh': 'Stronghold', 'sc': 'Scourge', '4e': 'Fourth Edition', 'isd' : 'Innistrad', 'dka' : 'Dark Ascension', 'avr' : 'Avacyn Restored', 'm13': 'Magic 2013', 'gtc': 'Gatecrash', 'dgm':"Dragon's Maze", 'm14':"Magic 2014"}

    kGameTypeStandard = 0
    kGameTypeCommander = 1
    kGameTypeDraft = 2
    kGameTypeTwoHeadedGiant = 4
    kGameTypeYuGiOh = 3
    kGameTypeRandomDecks = 5

    def port(self):
        return 4280
    
    def load_image(self,name):
        import pygame
        """ Load image and return image object"""
        image = pygame.image.load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image, image.get_rect()
    
    def VERSION(self):
        # Use Year.Month.Day[.subversion]
        return "13.9.10"

    def set_trace(self):
        '''Set a tracepoint in the Python debugger that works with Qt'''
        from PyQt4.QtCore import pyqtRemoveInputHook
        import pdb
        pyqtRemoveInputHook()
        pdb.set_trace()

utilities = Util()
