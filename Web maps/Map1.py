import folium
import pandas

map = folium.Map(location=[35.5, -110], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

for lt,ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=el,icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("Map1.html")