import csv
from Intersection import Intersection
import networkx as nx
import pylab
import dijkstra
import random
import helpers


def readData(numNodes):
    list_intersections = []
    dictionaryIdCoordinates = {}
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
                dictionaryIdCoordinates[int(line[5])] = [float(line[13]), float(line[14])]
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

def createGraph(numNodes):
    # Create the graph
    list_intersections, listAdjacency = createListAdjacency(numNodes)
    graph =  nx.Graph()

    # Add Nodes
    for i in list_intersections:
        graph.add_node(int(i.getIdBeginInter()), latitude =  i.getLatitudeInter(), longitude =  i.getLongitudeInter())


    weights = []
    # # Calculate weight
    # for i in range(len(list_intersections) - 1):
    #     distance = helpers.calculateDistanceBetweenTwoNodes(int(list_intersections[i].getLatitudeInter()),int(list_intersections[i].getLongitudeInter()), int(list_intersections[i + 1].getLatitudeInter()),int(list_intersections[i].getLongitudeInter()))

    #  Add Edges
    #graph.add_edges_from(listAdjacency)
    for i in range(len(listAdjacency)):
        graph.add_edge(int(listAdjacency[i][0]), int(listAdjacency[i][1]), weight = random.randint(1,50))

    return graph

# path = nx.shortest_path(graph, source = 1, target = 79, weight = "weight")
# length = nx.shortest_path_length(graph, source = 1, target = 79, weight = "weight")
# print(path, length)

def drawGraph(numNodes):
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


readData(10)