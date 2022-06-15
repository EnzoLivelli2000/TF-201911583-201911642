import csv
from ctypes.wintypes import RGB
from Node import Node
from Intersection import Intersection
from pyvis.network import *
import helpers
import networkx as nx
import matplotlib.pyplot as plt

list_intersections = []

# Read intersections
with open("Lima-intersecciones.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    cont = 0
    for line in csv_reader:
        if cont > 50:
            break
        else:
            intersection = Intersection(line[1], line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14])
            list_intersections.append(intersection)
            cont += 1

# Now create list adjacency
listAdjacency = []
listWeights = []
for i in list_intersections:
    list = []
    list.append(i.getidBeginInter()) # 1
    list.append(i.getidEndInter()) # 6
    listWeights.append(i.getDistance()) #  
    listAdjacency.append(list) # [[1,6], [6, 90275]], 
print(listAdjacency)
 

# Now create graph
graph = Network("1000px", "1000px", directed = True)
#graph2 =nx.Graph()


colorGenerate = ""
idBefore = 0

list_added = []

# Add vertices - node
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
    if not (list_intersections[i].getidBeginInter() in list_added):
        graph.add_node(list_intersections[i].getidBeginInter(), label = list_intersections[i].getidBeginInter(), x= list_intersections[i].getLatitudeInter(), y = list_intersections[i].getLongitudeInter(), title =list_intersections[i].getName(), color = colorRandom)
        list_added.append(list_intersections[i].getidBeginInter())

    if not (list_intersections[i].getidEndInter() in list_added):
        graph.add_node(list_intersections[i].getidEndInter(), label = list_intersections[i].getidEndInter(), x= list_intersections[i].getLatitudeInter(), y = list_intersections[i].getLongitudeInter(), title =list_intersections[i].getName(), color = colorRandom)
        list_added.append(list_intersections[i].getidEndInter())


# Add edges
for i in range(len(listAdjacency)):
    graph.add_edge(listAdjacency[i][0], listAdjacency[i][1], weight = 100, title = listWeights[i])
# Draw graph

#pos = nx.get_edge_attributes(graph2, "pos")
#nx.draw(graph2, pos)
#labels = nx.get_edge_attributes(graph2, "weight")
#nx.draw_networkx_edge_labels(graph2, pos, edge_labels=labels)
#plt.savefig(<wherever>)


graph.show_buttons(filter_=["physics"])
graph.show("lima.html")
