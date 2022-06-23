# In this file we check some functions and etc

# elements = {
#     1: [10, 20],
#     2: [30, 10]
# }
# print(elements[1][0])

# import folium
# import pandas as pd
# #import geopandas as gpd
# import numpy as np

# m = folium.Map()
# lista = [[(-12.0459308, -77.0427831), (-12.0460958, -77.0430896)],
#  [(-12.0460958, -77.0430896), (-12.0461253, -77.0431113)],
#  [(-12.0461253, -77.0431113), (-12.0462768, -77.0431753)],
#  [(-12.0462768, -77.0431753), (-12.0466033, -77.0431118)],
#  [(-12.0466033, -77.0431118), (-12.0466783, -77.0430483)],
#  [(-12.0466783, -77.0430483), (-12.0466949, -77.042435)],
#  [(-12.0466949, -77.042435), (-12.0465202, -77.0423222)],
#  [(-12.0465202, -77.0423222), (-12.0464537, -77.0423023)],
#  [(-12.0464537, -77.0423023), (-12.0462019, -77.0423251)],
#  [(-12.0462019, -77.0423251), (-12.0459528, -77.0425923)]]
# m.fit_bounds(lista)
# m.save("mapa.html")
# tooltip = "Haz click"
# for x in range(10):
#     var = lista[x][0]
#     folium.Marker(lista[x][0], popup=var, tooltip=tooltip, icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
# m.save("mapa.html")
# folium.PolyLine(
#     locations = lista,
#     popup = "Zona de paseo"
# ).add_to(m)
# m.save("mapa.html")