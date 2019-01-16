import os, EdgeClass, NodeClass

from myMethods import *

def main():
    global pathDij
    edgecounter = 0
    edgeread = []
    edgelist = []
    vertexlist = []
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
            edgelist.append(EdgeClass.Edge(distance, vertexlist[x], vertexlist[next-1], "edge{}.png".format(edgecounter)))
            end = len(edgelist)
            vertexlist[x].adjacenciesList.append(edgelist[end-1])
            edgeread.clear()
            edgecounter = edgecounter + 1

    files.close()
    start = None
    while start is None:
        os.system("cls")
        begin_value = input("Please enter the node where you wish start from (1-15): ")
        try:
            start = int(begin_value)
            if not (1 <= start <= 15):
                print("{input} is not between 1-15, please re-enter.".format(input=start))
                start = None
                os.system("PAUSE")
        except:
            print("{input} is not an integer, please re-enter your selection.".format(input=begin_value))
            os.system("PAUSE")
    finish = None
    while finish is None:
        os.system("cls")
        end_value = input("Please enter the where node you wish end on (1-15): ")
        try:
            finish = int(end_value)
            if not (1 <= finish <= 15):
                print("{input} is not between 1-15, please re-enter.".format(input=finish))
                finish = None
                os.system("PAUSE")
        except:
            print("{input} is not an integer, please re-enter your selection.".format(input=end_value))
            os.system("PAUSE")

    calculateshortestpath(vertexlist,vertexlist[finish - 1])
    getshortestpath(vertexlist[start - 1])
    buildpics(vertexlist)

    buildGif()
    edgecounter = 0
    repeat = None
    while repeat is None:
        input_value = input("Enter 1 to repeat the calculation or 2 to exit: ")
        try:
            repeat = int(input_value) # try and convert the string input to a number
            if (repeat == 1):
                os.system("cls")
                main()
            elif (repeat == 2):
                quit()
            else:
                repeat = None
        except ValueError:
            print("{input} is not a number, please enter a number only".format(input=input_value)) # Prompt to renter


main()
