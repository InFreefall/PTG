'''
Created on Jul 2, 2011

@author: mitchell
'''
class MinimalCard:
    def __init__(self, abbreviation, index, delegate=None, tapped=False):
        self.abbreviation = abbreviation
        self.index = index
        self.delegate = delegate
        self.tapped = tapped
