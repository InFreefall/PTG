'''
Created on Jul 8, 2011

@author: mitchell
'''

expansions = {'gp': 'Guildpact', 'zen': 'Zendikar', 'ala': 'Shards of Alara', 'row': 'Rise of the Eldrazi', 'lg': 'Legends', 'le': 'Legions', 'fve': 'From the Vault: Exiled', 'fvd': 'From the Vault: Dragons', 'tr': 'Torment', 'ts': 'Time Spiral', 'tp': 'Tempest', 'lw': 'Lorwyn', 'pch': 'Planechase', '5e': 'Fifth Edition', 'fvr': 'From the Vault: Relics', 'dm': 'Deckmasters', 'dk': 'The Dark', 'di': 'Disension', '9e': 'Ninth Edition', 'ds': 'Darksteel', 'cmd': 'Commander', 'eve': 'Eventide', 'evg': 'Duel Decks: Elves vs. Goblins', 'dpa': 'Duels of the Planeswalkers', 'shm': 'Shadowmoor', '10e': 'Tenth Edition', 'arb': 'Alara Reborn', 'arc': 'Archenemy', 'ex': 'Exodus', 'cfx': 'Conflux', 'tsts': 'Time Spiral "Timeshifted"', 'wwk': 'Worldwake', 'rv': 'Revised Edition', 'gvl': 'Duel Decks: Garruk vs. Liliana', 'ul': "Urza's Legacy", 'pd2': 'Premium Deck Series: Fire and Lightning', 'ddg': 'Duel Decks: Knights vs. Dragons', 'ddf': 'Duel Decks: Elspeth vs. Tezzeret', 'bd': 'Beatdown Box Set', 'be': 'Limited Edition Beta', '9eb': 'Ninth Edition Box Set', 'mgbc': 'Multiverse Gift Box Cards', 'ju': 'Judgment', 'wl': 'Weatherlight', '8e': 'Eighth Edition', 'br': 'Battle Royale Box Set', 'on': 'Onslaught', 'od': 'Odyssey', 'pds': 'Premium Deck Series: Slivers', 'bok': 'Betrayers of Kamigawa', 'ch': 'Chronicles', 'sok': 'Saviors of Kamigawa', 'som': 'Scars of Mirrodin', 'm11': 'Magic 2011', 'm10': 'Magic 2010', 'm12': 'Magic 2012', 'cs': 'Coldsnap', '5dn': 'Fifth Dawn', 'mbs': 'Mirrodin Besieged', 'pr': 'Prophecy', 'ps': 'Planeshift', 'chk': 'Champions of Kamigawa', 'pc': 'Planar Chaos', '6e': 'Sixth Edition', 'jvc': 'Duel Decks: Jace vs. Chandra', 'hl': 'Homelands', 'rav': 'Ravnica: City of Guilds', 'fut': 'Future Sight', 'mm': 'Mercadian Masques', 'mi': 'Mirrodin', 'pvc': 'Duel Decks: Phyrexia vs. The Coalition', 'us': "Urza's Saga", 'mt': 'Morningtide', 'un': 'Unlimited Edition', 'uh': 'Unhinged', 'mr': 'Mirage', 'ud': "Urza's Destiny", 'ug': 'Unglued', '7e': 'Seventh Edition', 'ai': 'Alliances', 'vi': 'Visions', 'al': 'Limited Edition Alpha', 'an': 'Arabian Nights', 'aq': 'Antiquities', 'ap': 'Apocalypse', 'at': 'Anthologies', 'in': 'Invasion', 'ia': 'Ice Age', 'uhaa': 'Unhinged Alternate Foils', 'ne': 'Nemesis', 'nph': 'New Phyrexia', '8eb': 'Eighth Edition Box Set', 'cstd': 'Coldsnap Theme Decks', 'fe': 'Fallen Empires', 'dvd': 'Duel Decks: Divine vs. Demonic', 'sh': 'Stronghold', 'sc': 'Scourge', '4e': 'Fourth Edition'}

input = ""
abbreviation = None

while True:
    if abbreviation is None:
        print "abbv> ",
    else:
        print "name> ",
    input = raw_input()
    if input == "quit":
        break
    if abbreviation is not None:
        expansions[abbreviation] = input
        abbreviation = None
    else:
        abbreviation = input
print "\nExpansion Dict:"
print expansions