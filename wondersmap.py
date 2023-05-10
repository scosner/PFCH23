import folium

m = folium.Map(location=[34.8984, 27.0828], zoom_start=4, tiles="Stamen Terrain")

tooltip = "Click me!"

#pyramid
folium.Marker(
    [29.9792, 31.1342], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/great-pyramid-of-giza>Great Pyramid of Giza</a>", tooltip=tooltip, 
).add_to(m)
#gardens
folium.Marker(
    [32.5427, 44.4217], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/hanging-gardens-of-babylon>Hanging Gardens of Babylon</a>", tooltip=tooltip
).add_to(m)
#Temple of Artemis
folium.Marker(
    [37.9485, 27.3689], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/temple-of-artemis-at-ephesus>Temple of Artemis at Ephesus</a>", tooltip=tooltip
).add_to(m)
#Zeus at Olympia
folium.Marker(
    [37.6379, 21.6308], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/statue-of-zeus-at-olympia>Statue of Zeus at Olympia</a>", tooltip=tooltip
).add_to(m)
#Halicarnassus
folium.Marker(
    [37.0380, 27.4246], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/mausoleum-at-halicarnassus>Mausoleum at Halicarnassus</a>", tooltip=tooltip
).add_to(m)
#Colossus
folium.Marker(
    [36.4510, 28.2270], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/colossus-of-rhodes>Colossus of Rhodes</a>", tooltip=tooltip
).add_to(m)
#Lighthouse
folium.Marker(
    [31.2156, 29.8850], popup="<a href=https://sites.google.com/pratt.edu/artancientwonders/wonders/lighthouse-of-alexandria>Lighthouse of Alexandria</a>", tooltip=tooltip
).add_to(m)


# Display the map
m
m.save('wondersmap.html')
