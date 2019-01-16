import os, os.path, webbrowser
import NodeClass, EdgeClass, PrimsMST
from myMethods import *

edgecounter = 0

def main():
    global pathDij
    global edgecounter
    edgeread = []
    edgelist = []
    vertexlist = []
#Scan once to create the Nodes
    filename = "Graph.txt"
    file = open(filename, "r")
    numberOfNodes = file.readline().strip()
    numberOfNodes = int(numberOfNodes)
    for x in range(numberOfNodes):
        nodeNumber = file.readline().strip()
        nodeNumber = int(nodeNumber)
        nodeName = file.readline().strip()
        vertexlist.append(NodeClass.Node(nodeName,nodeNumber))
        numberOfEdges = file.readline().strip()
        numberOfEdges = int(numberOfEdges)
        for i in range(numberOfEdges):
            edgeread.append(file.readline().strip())
            edgeread.clear()
    file.close()
    edgeread.clear()
#Scan twice to create the edges
    filename2 = "Graph.txt"
    files = open(filename2, "r")
    numberOfNodes = files.readline().strip()
    numberOfNodes = int(numberOfNodes)
    for x in range(numberOfNodes):
        nodeNumber = files.readline().strip()
        nodeNumber = int(nodeNumber)
        nodeName = files.readline().strip()
        numberOfEdges = files.readline().strip()
        numberOfEdges = int(numberOfEdges)
        for i in range(numberOfEdges):
            edgeread.append(files.readline().strip())
            edgeread = edgeread[0].split()
            next = edgeread[0]
            next = int(next)
            distance = edgeread[1]
            distance = float(distance)
            long = len(vertexlist)
            edgelist.append(EdgeClass.Edge(distance, vertexlist[x], vertexlist[next-1]))
            end = len(edgelist)
            vertexlist[x].adjacenciesList.append(edgelist[end-1])
            edgeread.clear()
            edgecounter = edgecounter + 1

    files.close()
    numNodes = len(vertexlist)
#Use vertexlist to build rows of matrix list initialized to 0
    for nodes in vertexlist:
        for i in range(numNodes):
            try:
                nodes.matrix.append(0)
            except:
                return
#Use vertexlist to insert edge weight into matrix list
    for nodes in vertexlist:
        for edges in nodes.adjacenciesList:
            nodes.matrix[edges.endvertex.number -1] = edges.weight
#Build 15x15 matrix list
    matrixBuild = []
    for nodes in vertexlist:
        matrixBuild.append(nodes.matrix)
    os.system("cls")
    print("This is the adjancey matrix of the graph:\n\n")
    for rows in matrixBuild:
        print(rows)
    print("\n\nThis is the Prim Minimum Spanning Tree: \n\n")
    g = PrimsMST.Graph(15)
    g.graph = matrixBuild
    g.primMST()
#Open pre-created .jpg of the MST 
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "AnchorageMST.jpg")
    webbrowser.open(path)

main()
