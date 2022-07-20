import folium
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=10)

# create a feature group
feature_group = folium.FeatureGroup(name="My Map")
# adding marker to feature group
feature_group.add_child(folium.Marker(
    location=[38.58, -99.09], popup="Hi i am a Marker", icon=folium.Icon(color='green')))


# adding multiple marker using for loop
lo = {"london": [38.3, -99.2], "nearby": [39.2, -98.2]}
for key, value in lo.items():
    feature_group.add_child(folium.Marker(
        location=value, popup=key, icon=folium.Icon(color='green')))

# add feature_group to map
map.add_child(feature_group)
map.save("map1.html")
