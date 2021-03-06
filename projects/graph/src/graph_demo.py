#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random


def createDefaultGraph():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(2)
    graph.add_vertex(6)
    graph.add_vertex(1)
    graph.add_vertex(4)
    graph.add_vertex(7) 
    graph.add_vertex(3)
    graph.add_vertex(10)
    graph.add_vertex(11)
    graph.add_edge(5, 2)
    graph.add_edge(5, 6)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(4, 3)
    graph.add_edge(6, 7)

    # print(f"This is DFT:\n{graph.dft(5)}")
    print(f"This is BFS:\n{graph.bfs(5, 3)}")
    print(f"This is DFS-Recursive:\n{graph.dfs(5, 6)}")
    print(f"This is BFS-Path:\n{graph.bfs_path(10, 3)}")
    print(f"This is DFS-Path:\n{graph.dfs_path(5, 3)}")
    # bg = BokehGraph(graph)
    # bg.draw()

def createRandomGraph(numNodes, numEdges):
    graph = Graph()

    all_edges = []
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i, j) )
    
    random.shuffle(all_edges)
    edges = all_edges[:numEdges]

    if numEdges > len(all_edges):
        print("Too many edges")
    
    for edge in edges:
        print(edge)
    
    for i in range(numNodes):
        graph.add_vertex(i)

    for edge in edges:
        print(edge)
        graph.add_edge(edge[0], edge[1])

    print(len(edges))

    bg = BokehGraph(graph)
    bg.draw()


def main(style, numNodes, numEdges):
    if style == "default":
        createDefaultGraph()
    elif style == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    # parse argv
    style = "default"
    numNodes = 5
    numEdges = 5

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                numNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                numEdges = int(arg_split[1])
            else:
                print("\nInvalid command.\n")

    main(style, numNodes, numEdges)