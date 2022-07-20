import pandas
import folium

# load data
data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
elv = list(data.ELEV)
name = list(data.NAME)

print(data.ELEV.max())

# popup html
html = """<h4>Volcano information: <br/>
     Name: %s <br />
    Height : %s m
</h4> """

# create map
map = folium.Map(zoom_start=23)
fg = folium.FeatureGroup(name="My Map")


def return_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# using zip to loop throuh 2 list at once
for lt, ln, el, nm in zip(lat, lon, elv, name):
    iframe = folium.IFrame(html=html % (nm, el), width=250, height=100)
    fg.add_child(folium.Marker(location=[lt, ln],
                 popup=folium.Popup(iframe), icon=folium.Icon(color=return_color(el))))


map.add_child(fg)
map.save("volcano.html")
