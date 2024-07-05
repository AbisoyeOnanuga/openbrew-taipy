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
    "size": "size",
    "color": "color",
    "text": "text",
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
    },
        "annotations": [
        {
            "x": 1.0,
            "y": 1.2,
            "xref": "paper",
            "yref": "paper",
            "text": "Type of Brewery",
            "showarrow": False,
            "font": {"size": 24}
        },
        {
            "x": 0.939,
            "y": 1.0,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Micro",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#6f4e37"}
        },
        {
            "x": 0.939,
            "y": 0.9,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Nano",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#ffd700"}
        },
        {
            "x": 0.959,
            "y": 0.8,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Regional",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#0000ff"}
        },
        {
            "x": 0.96,
            "y": 0.7,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Brewpub",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#ff4500"}
        },
        {
            "x": 0.942,
            "y": 0.55,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Large",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#808080"}
        },
        {
            "x": 0.96,
            "y": 0.45,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Planning",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#008000"}
        },
        {
            "x": 0.929,
            "y": 0.35,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Bar",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#808080"}
        },
        {
            "x": 0.96,
            "y": 0.2,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Contract",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#800080"}
        },
        {
            "x": 0.969,
            "y": 0.1,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Proprietor",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#ffa500"}
        },
        {
            "x": 0.949,
            "y": 0,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Closed",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "#ff0000"}
        }
    ]
}

map_md = Markdown("pages/map/map.md")
