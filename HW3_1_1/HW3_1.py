import Trie   # Imports trie module, trie.py
import random   # You will want this to generate random numbers
from random import choice
import os
def main():
    t = Trie.TrieNode()         # Create the root node
    t.build()

    while len(Trie.randomWord) < 100:
        t.randomLookUp()
    os.system("cls")
    print("This is Part 1: 100 random words from Alice in Wonderland, please notice that there are no repeat words.\n")
    t.printRandom()
    print("\n\n")
# Start running main
main()
