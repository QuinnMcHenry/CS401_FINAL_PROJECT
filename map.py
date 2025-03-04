import folium
from folium.plugins import MousePosition

m = folium.Map(location = [21.485, 202.017], zoom_start = 11, min_zoom = 11, dragging = True)


tile_url = "https://api.mapbox.com/styles/v1/quinndaniel11/clp0j258c00cn01of0uzodeg3/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoicXVpbm5kYW5pZWwxMSIsImEiOiJjbTd0djgzNG0yMDhoMmtwdnBxb3V3d3E4In0.aqOJFJsCFNI_cBcmZ46f7A"

# Add the custom tile layer
folium.TileLayer(
    tiles=tile_url,
    attr="Mapbox Outdoors",
    name="Custom Mapbox",
    min_zoom = 11,
    max_zoom = 19
).add_to(m)

m.save("map.html")
