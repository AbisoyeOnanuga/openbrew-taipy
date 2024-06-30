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

stylekit = {
    "color_primary": "rgb(0, 123, 255)",  # A blue-ish primary color
    "color_secondary": "rgb(255, 193, 7)",  # Example secondary color
    "color_background_light": "rgb(240, 248, 255)",  # A light blue background for the light theme
    "color_background_dark": "rgb(29, 36, 75)",  # Dark blue for dark theme background
    "color_paper_dark": "rgb(55, 55, 55)",  # Darker grey for elevated elements in dark theme
    "color_paper_light": "rgb(255, 255, 255)",  # White for elevated elements in light theme
    "color-contrast-dark": "rgb(248, 217, 217)", # Contrasting elements (such as text) color for dark backgrounds
    "color-contrast-light": "rgb(43, 15, 58)", # Contrasting elements (such as text) color for light backgrounds
    "font_family": "'Roboto', sans-serif",  # Example font family
    # ... other style properties ...
}

# Create the Gui instance with the Markdown pages
gui_multi_pages = Gui(pages=pages, css_file="styles.css")

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="Breweries in United States", stylekit=stylekit)
