import heapq, sys

import webbrowser
pathDij = []
piclist = []

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def calculateshortestpath(vertexlist, startvertex):
    q = []
    startvertex.mindistance = 0
    heapq.heappush(q, startvertex)
    while q:
        actualnode = heapq.heappop(q)
        for edge in actualnode.adjacenciesList:
            #print("mindistance" , edge.startvertex.mindistance , "weight", edge.weight)
            tempdist = edge.startvertex.mindistance + edge.weight
            if tempdist < edge.endvertex.mindistance:
                edge.endvertex.mindistance = tempdist
                edge.endvertex.predecessor = edge.startvertex
                heapq.heappush(q,edge.endvertex)

def getshortestpath(targetvertex):
    global pathDij
    print("The value of it's minimum distance is: ",targetvertex.mindistance)
    node = targetvertex
    while node:
        pathDij.append(node.number)
        node = node.predecessor
    print("Dijkstra's Path =", pathDij)
    pathDij.clear()
