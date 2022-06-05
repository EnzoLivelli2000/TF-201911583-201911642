import csv
from ctypes.wintypes import RGB
from Node import Node
from Intersection import Intersection
from pyvis.network import *
import helpers

list_intersections = []

# Read intersections
with open("Lima-intersecciones.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    cont = 0
    for line in csv_reader:
        if cont > 200:
            break
        else:
            intersection = Intersection(line[1], line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14])
            list_intersections.append(intersection)
            cont += 1

# Now create list adjacency
listAdjacency = []
for i in list_intersections:
    list = []
    for j in list_intersections:
        if i.getidEndInter() == j.getidBeginInter():
            list.append(i.getidBeginInter())
            list.append(j.getidBeginInter())
    if len(list) > 1:
        listAdjacency.append(list)

# Now create graph
graph = Network("1000px", "1000px", directed = True)


colorGenerate = ""
idBefore = 0

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
    graph.add_node(list_intersections[i].getidBeginInter(), label = list_intersections[i].getidBeginInter(), x= list_intersections[i].getLatitudeInter(), y = list_intersections[i].getLongitudeInter(), title =list_intersections[i].getName(), color = colorRandom)

# Add edges
for i in listAdjacency:
    graph.add_edge(i[0], i[1], weight =.87)
# Draw graph
graph.show_buttons(filter_=["physics"])
graph.show("lima.html")
