import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printMST(self, parent):
        mstWeight = 0
        print ("Edge \t\tWeight")
        for i in range(1,self.V):
            print (parent[i]+1," - ",i+1,"\t",self.graph[i][ parent[i] ])
            mstWeight += self.graph[i][ parent[i] ]
        print("\nWeight of MST:\t", mstWeight)

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for i in range(self.V):
            if key[i] < min and mstSet[i] == False:
                min = key[i]
                minIndex = i

        return minIndex

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = 0
        for x in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.printMST(parent)
