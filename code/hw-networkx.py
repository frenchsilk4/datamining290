#!/usr/bin/python
import networkx as nx

import pylab as p



class Node(int):
    nodes = []

    def __init__(self, label):
        self._label = label

    def __str__(self):
        return self._label

nodes = [Node(l) for l in ["1","2","3","4","5","6"]]
edges = [(6,4),(4,5),(5,1),(1,2),(2,3),(3,4)]

G = nx.Graph()
for i,j in edges:
    G.add_edge(nodes[i-1], nodes[j-1])

print(nx.adjacency_matrix(G,nodelist=None,weight=None))
