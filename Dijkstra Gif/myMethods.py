import heapq, subprocess, sys, os.path, webbrowser
import moviepy.editor as mpy
from moviepy.editor import *

pathDij = []
piclist = []

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

def buildpics(vertexlist):
    for i,item in enumerate(pathDij):
        for nodes in vertexlist:
            if (item == nodes.number):
                for now, edges in enumerate(nodes.adjacenciesList):
                    if  (edges.startvertex.number == item):
                        try:
                          if (edges.endvertex.number == pathDij[i+1]):
                              piclist.append(edges.picture)
                        except:
                            ()
                            exit

def buildGif():
    gif_name = 'AnchorageMap1'
    fps = 1
    clip = mpy.ImageSequenceClip(piclist, fps=fps)
    clip.write_gif('{}.gif'.format(gif_name), fps=fps)
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "AnchorageMap1.gif")
    webbrowser.open(path)
    pathDij.clear()
    piclist.clear()
