# Brewery Data Exploration with Taipy
## Overview
This project demonstrates how to build a multipage web application using Taipy to explore data from the Open Brewery DB API at <a href="https://openbrewerydb.org">Open Brewery DB</a>. The app includes a list view, a dashboard, and a map view, all styled with custom CSS and Taipy’s Stylekit.

## Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Application Structure](#application-structure)
3. [Detailed Component Guides](#detailed-component-guides)

## Setup Instructions

### Prerequisites
- Python 3.x
- Taipy library
- Pandas
- Requests

### Installation
1. Clone the repository:
```bash
    git clone <repository-url>
    cd <repository-directory>
```

2. Install the required libraries:
`pip install taipy pandas requests`

## Application Structure
```bash
    .
    ├── main.py
    ├── pages
    │   ├── data
    │   │   ├── data.py    
    │   │   └── README.md
    │   ├── table
    │   │   ├── table.py
    │   │   ├── table.md    
    │   │   └── README.md
    │   ├── dashboard
    │   │   ├── dashboard.py
    │   │   ├── dashboard.md
    │   │   └── README.md
    │   ├── map
    │   │   ├── map.py
    │   │   ├── map.md
    │   │   └── README.md
    │   ├── root
    │   │   ├── root.py
    │   │   ├── root.md
    │   │   └── README.md
    ├── styles.css
    └── README.md
```

## Detailed Component Guides
For detailed guides on each component, refer to the following links:

- [**Style Guide**](./README-STYLE.md): Information on the stylekit and custom CSS.
- [**Root Guide**](./README-ROOT.md): Detailed guide for root.py and root.md.
- [**Data Guide**](./README-DATA.md): Detailed instructions for data fetching and preparation.
- [**Table Guide**](./README-TABLE.md): Information on the table view and its implementation.
- [**Dashbaord Guide**](./README-DASHBOARD.md): Guide for the dashboard view and its components.
- [**Map Guide**](./README-MAP.md): Detailed instructions for the map view and its setup.

### main.py
This is the main entry point of the application. It sets up the pages and the stylekit.
```python
    from taipy.gui import Gui
    import taipy as tp

    # Import the Markdown pages
    from pages.root import root, selected_location, selector_location
    from pages.table.table import table_md
    from pages.dashboard.dashboard import dashboard_md
    from pages.map.map import map_md

    # Define the pages dictionary with the Markdown pages
    pages = {
        '/': root,
        "List": table_md,
        "Dashboard": dashboard_md,
        "Map": map_md,
    }

    # Function to inject JavaScript into the HTML
    def inject_js(html_content):
        script_tag = '<script src="/static/fix_links.js"></script>'
        return html_content.replace('</body>', f'{script_tag}</body>')

    stylekit = {
        "color_primary": "rgb(140, 110, 80)",  # A rich brown color reminiscent of beer
        "color_secondary": "rgb(200, 180, 140)",  # A lighter complementary color
        "color_background_light": "rgb(255, 248, 240)",  # A warm light background for the light theme
        "color_background_dark": "rgb(50, 40, 30)",  # Dark brown for dark theme background
        "color_paper_dark": "rgb(75, 65, 55)",  # Darker brown for elevated elements in dark theme
        "color_paper_light": "rgb(255, 255, 255)",  # White for elevated elements in light theme
        "color-contrast-dark": "rgb(255, 235, 205)",  # Cream color for contrasting elements on dark backgrounds
        "color-contrast-light": "rgb(50, 40, 30)",  # Dark brown for contrasting elements on light backgrounds
        "color_background_odd_row": "#f2f2f2",  # Light grey for odd row background
        "color_text_odd_row": "#333333",  # Dark grey for odd row text
        "font_family": "'Georgia', serif",  # A font that gives a classic feel
        # ... other style properties ...
    }

    # Create the Gui instance with the Markdown pages
    gui_multi_pages = Gui(pages=pages, css_file="styles.css")

    if __name__ == '__main__':
        tp.Core().run()
        
        gui_multi_pages.run(title="Breweries in United States", stylekit=stylekit)
```

## Features

- **Table Page**: A comprehensive table listing all the breweries with sortable columns.
- **Dashboard Page**: Visual analytics of brewery data including charts and graphs.
- **Map Page**: An interactive map displaying the geographical distribution of breweries.

## Getting Started

To get started with OpenBrew-Taipy, clone this repository and install the required dependencies.

```bash
git clone https://github.com/your-username/openbrew-taipy.git
cd openbrew-taipy
pip install -r requirements.txt
```
