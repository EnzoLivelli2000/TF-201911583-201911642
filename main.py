import csv
#from igraph import *
from Intersection import Intersection
from pyvis.network import *

list_intersections = []

# Read intersections
with open("Lima-intersecciones.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    cont = 0
    for line in csv_reader:
        if cont > 11:
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
        listAdjacency.append(tuple(list))

# Now create graph
graph = Network("500px", "500px")

# Add vertices - node
for i in listAdjacency:
    graph.add_node(i[0], label = i[0])

# Add edges
for i in listAdjacency:
    graph.add_edge(i[0], i[1], weight =.87)

graph.show("lala.html")
