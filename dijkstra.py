import heapq as hq
import math
import numpy as np
import networkx as nx
from graph import createGraph, createListAdjacency, getWeightsEdges, readData
from helpers import createMap

def dijkstraAlgorithm(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n

  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v]:
          f = g + w
          if f < cost[v]:
            cost[v] = f
            path[v] = u
            hq.heappush(pqueue, (f, v))

  return path, cost

def calculateShortestRouteBetweenTwoNodes(target):
    graph = createGraph(100)
    coordinates = []
    path = nx.shortest_path(graph, source = 1, target = target, weight = "weight")
    length = nx.shortest_path_length(graph, source = 1, target = target, weight = "weight")
    for i in path:
      lista = []
      tuplaOne = (graph.nodes[i]["latitudeBegin"], graph.nodes[i]["longitudeBegin"])
      tuplaTwo = (graph.nodes[i]["latitudeEnd"], graph.nodes[i]["longitudeEnd"])
      lista.append(tuplaOne)
      lista.append(tuplaTwo)
      coordinates.append(lista)
    createMap(coordinates)
