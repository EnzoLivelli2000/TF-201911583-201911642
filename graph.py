import csv
from Intersection import Intersection
import networkx as nx
import pylab

list_intersections = []

# Read intersections
with open("./data/Lima-intersecciones.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    cont = 0
    for line in csv_reader:
        if cont > 10:
            break
        else:
            intersection = Intersection(line[1], line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14])
            list_intersections.append(intersection)
            cont += 1

# Now create list adjacency
listAdjacency = []
listWeights = []
for i in list_intersections:
    tuple = (i.getIdBeginInter(), i.getIdEndInter())
    listWeights.append(i.getDistance()) #  
    listAdjacency.append(tuple) # [[1,6], [6, 90275]], 



# Create the graph
graph =  nx.Graph()

# Add Nodes
for i in list_intersections:
    graph.add_node(i.getIdBeginInter(), node_color = "red")

#  Add Edges
graph.add_edges_from(listAdjacency)

# options = {
#     "node_size": 50,
#     "node_color": "black"
# }

nx.draw(graph, with_labels=True)
pylab.show()
