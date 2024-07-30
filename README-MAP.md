# Map Guide

## Overview
The `map.py` file handles the map view of the Brewery Data Exploration app. It visualizes brewery locations across the United States, providing an interactive map with detailed information about each brewery.

## Code Explanation
### map.py
```python
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
                "font": {"size": 16, "color": "#c8b560"}
            },
            {
                "x": 0.959,
                "y": 0.8,  # Adjusted for more spacing
                "xref": "paper",
                "yref": "paper",
                "text": "● Regional",  # Larger bullet point using Unicode
                "showarrow": False,
                "font": {"size": 16, "color": "#add8e6"}
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
                "font": {"size": 16, "color": "#8A2BE2"}
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
```
- Data Initialization: Fetches the brewery data using the `fetch_data` function from the `data` module and prepares it for the map using the `prepare_map_data` function.
- Hover Label: Defines the hover label properties for the map markers.
- Marker: Configures the marker properties, including size, color, text, and hover information.
- Layout: Sets up the layout for the map, including the title, geographic settings, and annotations for the brewery types.
- Markdown Content: Defines the map page content using a Markdown file.

### map.md
The `map.md` file contains the Markdown content for the map page.
```markdown
    # **US Breweries**{: .color-primary} Map

    <|{map_data}|chart|type=scattergeo|mode=markers|lat=Latitude|lon=Longitude|marker={marker}|text=text|layout={layout}|>
    <br/><br/>

    The brewery type map displays various types of breweries across the United States. Each marker represents a specific type of brewery:

    - **<span style="color:#6f4e37">Micro</span>**: Most craft breweries. For example, Samual Adams is still considered a microbrewery.
    - **<span style="color:#c8b560">Nano</span>**: An extremely small brewery which typically only distributes locally.
    - **<span style="color:#add8e6">Regional</span>**: A regional location of an expanded brewery (e.g., Sierra Nevada’s Asheville, NC location).
    - **<span style="color:#ff4500">Brewpub</span>**: A beer-focused restaurant or restaurant/bar with a brewery on-premise.
    - **<span style="color:#8A2BE2">Large</span>**: A very large brewery (likely not for visitors, e.g., Miller-Coors).
    - **<span style="color:#008000">Planning</span>**: A brewery in planning or not yet opened to the public.
    - **<span style="color:#808080">Bar</span>**: A bar with no brewery equipment on premise (deprecated).
    - **<span style="color:#800080">Contract</span>**: A brewery that uses another brewery’s equipment.
    - **<span style="color:#ffa500">Proprietor</span>**: Similar to contract brewing but refers more to a brewery incubator.
    - **<span style="color:#ff0000">Closed</span>**: A location which has been closed.

    Explore the map to discover the rich diversity of brewing styles and learn about the unique characteristics of each type.
```
- Map Visualization: Displays the brewery locations on a scattergeo chart with markers.
- Brewery Types: Provides a legend explaining the different types of breweries, each with a specific color.
