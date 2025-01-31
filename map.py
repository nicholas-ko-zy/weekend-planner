"""
Create an interactive map given the location of several places.
Places:
1. The Projector
2. Asian Film Archive @ The National Archives Building
3. Peatix
4. The Esplanade
"""
import folium
import branca

m = folium.Map(location=(1.3021, 103.8641), # Coordinates of The Projector
               # Show scale at the bottom of the map
               control_scale=True,
               # Turn off default OSM basemap tiles
               tiles=None,
               zoom_start=20)

folium.TileLayer("OpenStreetMap", control=False)

# Add Esri Satellite image as the tile layer over the basemap
folium.TileLayer("Esri.WorldImagery").add_to(m)
folium.TileLayer(show=False).add_to(m)


"""Create a FeatureGroup, which as its name implies, is a group of features that
you can overlay on the map"""
fg = folium.FeatureGroup(name="Venues", control=True).add_to(m)


# Add an Iframe Popup that brings you to The Projector Site to see what's
# showing that week
html_projector = """
<iframe src="https://theprojector.sg/" width="100%" style="border: none;"></iframe>"
"""

iframe = branca.element.IFrame(html=html_projector, width=500, height=300)
popup_projector = folium.Popup(iframe, max_width=500)

folium.Marker(
    location=[1.3021, 103.8641],
    tooltip="The Projector",
    popup=popup_projector,
    icon=folium.Icon(color='red'),
).add_to(fg)

# Add LayerControl: An option that you can toggle layers on the map
folium.LayerControl().add_to(m)

# Save map to html, since I'm using an IDE, not a notebook.
m.save("index.html")

