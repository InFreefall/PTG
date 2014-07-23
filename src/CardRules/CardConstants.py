def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

CardType = enum('Artifact','Creature','Enchantment','Instant','Basic Land','Land','Plane','Planeswalker','Scheme','Sorcery','Tribal','Vanguard')
CardSubtype = enum('Angel','Human','Wizard','Archer','Archon','Horse','Griffin','Soldier','Cleric','Knight','Druid','Cat','Monk','Rhino','Siren','Salamander','Rogue','Bird','Sphinx','Drake','Merfolk','Djinn','Giant','Serpent','Vedalken','Bear','Illusion','Dragon','Vampire','Shaman','Warrior','Zombie','Insect','Shade','Bat','Skeleton','Assassin','Demon','Spirit','Ogre','Elemental','Hound','Goblin','Minotaur','Berserker','Wall','Ooze','Spider','Boar','Wurm','Troll','Treefolk','Elf','Beast','Scout','Basilisk','Crocodile','Hydra','Wolf','Construct','Golem','Aura','Gideon','Jace','Sorin','Chandra','Garruk','Swamp','Plains','Forest','Island','Mountain')
