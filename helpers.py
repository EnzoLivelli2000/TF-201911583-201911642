import random
from math import sin, cos, sqrt, atan2, radians
import folium
import pandas as pd
#import geopandas as gpd
import numpy as np


# This function generate a random color 
def random_color():
    colorRandom = "#"
    letters = ['a', 'b', 'c', 'd', 'e']
    for i in range(6):
        option = random.randint(1,2)
        if option == 1: # Generate a random number between 0-9
            colorRandom += str(random.randint(0,9))
        else:
            numberPosition = random.randint(0,4)
            colorRandom += letters[numberPosition]
    return colorRandom

def calculateDistanceBetweenTwoNodes(lat1, lon1, lat2, lon2):
    R = 6373.0
    
    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def trafficFactor():
    print("Hi")

def createMap(lista):
    m = folium.Map()
    m.fit_bounds(lista)
    m.save("mapa.html")
    tooltip = "Haz click"
    for x in range(10):
        var = lista[x][0]
        folium.Marker(lista[x][0], popup=var, tooltip=tooltip, icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
    m.save("mapa.html")
    folium.PolyLine(
        locations = lista,
        popup = "Zona de paseo"
    ).add_to(m)
    m.save("mapa.html")