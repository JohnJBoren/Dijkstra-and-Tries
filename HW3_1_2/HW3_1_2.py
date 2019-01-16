import Trie   # Imports trie module, trie.py
import random   # You will want this to generate random numbers
from random import choice
import os
def main():
    t = Trie.TrieNode()         # Create the root node
    t.build()
    os.system("cls")
    print("This is Part 2")
    while len(Trie.randomWord) < 1:
        t.randomLookUp()
    randword = random.choice(Trie.randomWord)
    print()
    t.printRandomBetter(randword)
# Start running main
main()
