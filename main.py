import csv
#from igraph import *
from Intersection import Intersection
from pyvis.network import *

list_intersections = []

nodes = []

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
            nodes.append(line[5])
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
graph = Network("1000px", "1000px")

# Add vertices - node
for i in nodes:
    graph.add_node(i, label = i)
# Add edges
for i in listAdjacency:
    graph.add_edge(i[0], i[1], weight =.87)
# Draw graph
graph.show_buttons(filter_=["physics"])
graph.show("lima.html")
