from taipy.gui import Gui
import taipy as tp

# Import the Markdown pages
from pages.root import root, selected_location, selector_location
from pages.table.xhtml_table import table
from pages.dashboard.dashboard import dashboard_md
from pages.map.map import map_md

# Define the pages dictionary with the Markdown pages
pages = {
    '/': root,
    "List": table,
    "Dashboard": dashboard_md,
    "Map": map_md,
}

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
