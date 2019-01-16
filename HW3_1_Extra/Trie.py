# This is the Trie module with a TrieNode class.
# It implements a trie for ASCII words read from a text file. The words
# may include punctuation.

import random   # You will want this to generate random numbers
from random import choice
# Implementation of a trie.  TrieNode objects make up the nodes of the trie.
# A node has:
#    children:  A dictionary where the key is the letter and the value is a child TrieNode.
#               For example, if there is a link for letter 'a' then {a : TrieNode}
#               is stored in the dictionary.  This is easier to manage than a list or
#               array.
#    endsOnWord: Set to False initially.  If the TrieNode marks the end of a word,
#               then endsOnWord is set to the complete word.
randomWord = []
mainwordlist = []
newwordlist = []
counter = 0
class TrieNode:
    def __init__(self):
        self.children = {}  # Empty dictionary, stores letters for indexing children
        self.endsOnWord = False  # Marks if this is the last letter of a word
        self.beenHere = False
        self.Nextwords = []

    def build(self):
        wordlist1 = self.readWords()
        for position, word in enumerate(wordlist1):
            self.insert(word,position)

    def readWords(self):
        global mainwordlist
        with open('alice.txt','r') as f:     # CHANGE to selected text file
            for line in f:
                for word in line.split():
                   mainwordlist.append(word.lower())
        return mainwordlist

    # inserts a new word into the trie.  It calls the recursive method _insert.
    def insert(self, word, position):
        self._insert(word, word, position)

    # _insert recursively traverses the trie. It takes the first letter off
    # variable 'word' to retrieve the corresponding dictionary entry to a child.
    # It then recurses on the rest of the word.  For example, if the word is
    # "romeo" then the c = "r" and rest ="omeo" for traversing the rest of the trie.
    def _insert(self, word, originalWord, position):
        if len(word)>0:
            c = word[0]      # first character of the string
            rest = word[1:]  # Rest of the string from index 1 to end
            if c in self.children:  # True if there is a key entry in the dictionary with c
                # Child already exists with first letter, recurse on child
                self.children[c]._insert(rest, originalWord, position)
            else:
                # No child of first letter, create one
                self.children[c] = TrieNode()
                self.children[c]._insert(rest, originalWord, position)
        else:
            # This is an empty node that marks the end of the word.
            self.endsOnWord = originalWord  # Marks that this node is the end of a word with the word itself
#---HW3_1_Extra Credit  The way the insert to my nextwords list includes every word that came after the given word.  Frequency is accounted for.
            self.Nextwords.append(position + 1)
    # Prints out the trie recursively using indentation for each level.
    # Only do this or a small trie.
    def print(self, level = 0):
        # Indent based on the level in the trie
        for __ in range(0,level):    # __ is used for throwaway/anonymous vars
            print("  ",end="")
        print("Level:",level,". EndsOnWord:",self.endsOnWord,". Node Address:",self)
        for __ in range(0,level):    # __ is used for throwaway/anonymous vars
            print("  ",end="")
        print("Children:",self.children)
        for k in self.children:
            self.children[k].print(level+1)

    # Recursively looks up the word in the trie.  If found, returns the
    # TrieNode that terminates the word in the trie.  Otherwise, returns False.
    def lookup(self, word):
        if len(word)>0:
            c = word[0]
            rest = word[1:]
            if c in self.children:
                return self.children[c].lookup(rest)
            return False
        else:
            if self.endsOnWord != False:
                return random.choice(self.Nextwords)
        return False

    def printRandom(self):
        global randomWord
        for x in randomWord:
            print(x, end = " ")
        randomWord.clear()

    def printRandomBetter(self, x):
        global counter
        while (counter < 100):
            next = self.lookup(x)
            nextw = mainwordlist[next]
            print(x, end = " ")
            counter += 1
            return self.printRandomBetter(nextw)

    def randomLookUp(self):
        a = list(self.children.keys())
        if len(a) == 0:
            return self
        else:
            w = random.choice(a)
            if (self.endsOnWord) and (random.random() < 0.5) and (not self.beenHere) and (self.endsOnWord != None):
                randomWord.append(self.endsOnWord)
                self.beenHere = True
                return self.endsOnWord
            else:
                self.children[w].randomLookUp()
