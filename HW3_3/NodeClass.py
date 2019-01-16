import sys
class Node:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.visited = False
        self.adjacenciesList = []
        self.predecessor = None
        self.mindistance = sys.maxsize
        self.matrix = []

    def __lt__(self, other):
        return self.mindistance < other.mindistance
