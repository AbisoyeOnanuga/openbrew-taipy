from taipy.gui import Markdown
from ..data.data import fetch_data, prepare_map_data

# Fetch the data and prepare the map data
data = fetch_data()
map_data = prepare_map_data(data)

hoverlabel = {
    "bgcolor": "rgba(128, 128, 128, 0.5)",
    "bordercolor": "black",
    "font": {"color": "black", "size": 12},
    "align": "left"
}

marker = {
    "size": map_data["size"],
    "color": map_data["color"],
    "text": map_data["text"],
    "textposition": "bottom center",
    "hoverinfo": "text",
    "hoverlabel": hoverlabel
}

layout = {
    "title": "Brewery Locations in the US<br>(Hover for details)",
    "geo": {
        "showland": True,
        "landcolor": "lightgrey",
        "countrycolor": "darkgrey",
        "fitbounds": "locations",
        "projection_type": "mercator"
    }
}

map_md = Markdown("pages/map/map.md")
