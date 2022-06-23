import csv
from matplotlib.pyplot import draw
from nbformat import read
from Intersection import Intersection
import networkx as nx
import pylab
import helpers
from pyvis.network import *

def readData(numNodes):
    list_intersections = []
    # Read intersections
    with open("./data/Lima-intersecciones.csv", "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        cont = 0
        for line in csv_reader:
            if cont > numNodes:
                break
            else:
                intersection = Intersection(line[1], line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14])
                list_intersections.append(intersection)
                cont += 1
    return list_intersections

def createListAdjacency(numNodes):
    list_intersections = readData(numNodes)
    # Now create list adjacency
    listAdjacency = []
    listWeights = []
    for i in list_intersections:
        tuple = (i.getIdBeginInter(), i.getIdEndInter())
        listWeights.append(i.getDistance()) #  
        listAdjacency.append(tuple) # [[1,6], [6, 90275]], 
        
    return list_intersections, listAdjacency

def getWeightsEdges(numNodes):
    list_intersections = readData(numNodes)
    weights = []
    # Calculate weight
    for i in range(len(list_intersections)):
        distance = helpers.calculateDistanceBetweenTwoNodes(float(list_intersections[i].getLatitudeBeginInter()),float(list_intersections[i].getLongitudeBeginInter()),float(list_intersections[i].getLatitudeEndInter()),float(list_intersections[i].getLongitudeEndInter()))
        weights.append(distance)
    return weights


def createGraph(numNodes):
    # Create the graph
    list_intersections, listAdjacency = createListAdjacency(numNodes)
    weights = getWeightsEdges(numNodes)
    graph =  nx.Graph()

    # Add Nodes
    for i in list_intersections:
        graph.add_node(int(i.getIdBeginInter()), id = i.getIdBeginInter(), latitudeBegin =  i.getLatitudeBeginInter(), longitudeBegin =  i.getLongitudeBeginInter(), latitudeEnd =  i.getLatitudeEndInter(), longitudeEnd =  i.getLongitudeEndInter())

    #  Add Edges
    #graph.add_edges_from(listAdjacency)
    for i in range(len(listAdjacency)):
        graph.add_edge(int(listAdjacency[i][0]), int(listAdjacency[i][1]), weight = weights[i])

    return graph


def drawGraphOne(numNodes):
    graph = createGraph(numNodes)
    # Draw Graph
    pos = nx.spring_layout(graph)
    # Draw nodes
    nx.draw_networkx_nodes(graph, pos)
    # Draw edges
    nx.draw(graph, pos)
    # Labels nodes and edges
    nx.draw_networkx_labels(graph, pos)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    # Dhow graph
    pylab.show()

def drawGraphTwo(numNodes):
    list_intersections, listAdjacency = createListAdjacency(numNodes)
    weights = getWeightsEdges(numNodes)
    # Now create graph
    graph = Network("1000px", "1000px", directed = True)

    colorGenerate = ""
    idBefore = 0

    list_added = []

    # Add node
    for i in range(len(list_intersections)):
        colorRandom = helpers.random_color()
        if colorGenerate == "":
            colorGenerate = colorRandom
            idBefore = list_intersections[i].getId()
        elif idBefore == list_intersections[i].getId() and i > 0:
            colorRandom = colorGenerate
        else:
            idBefore = list_intersections[i].getId()
            colorGenerate = colorRandom
        # Insert Nodes
        if not (list_intersections[i].getIdBeginInter() in list_added):
            graph.add_node(list_intersections[i].getIdBeginInter(), label = list_intersections[i].getIdBeginInter(), title =list_intersections[i].getName(), color = colorRandom)
            list_added.append(list_intersections[i].getIdBeginInter())

        if not (list_intersections[i].getIdEndInter() in list_added):
            graph.add_node(list_intersections[i].getIdEndInter(), label = list_intersections[i].getIdEndInter(), title =list_intersections[i].getName(), color = colorRandom)
            list_added.append(list_intersections[i].getIdEndInter())
    # # Add edges
    for i in range(len(listAdjacency)):
        graph.add_edge(listAdjacency[i][0], listAdjacency[i][1], title = weights[i])
    # Draw graph
    graph.show_buttons(filter_=["physics"])
    graph.show("lima.html")
