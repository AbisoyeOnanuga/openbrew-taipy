import pandas as pd
from taipy.gui import Markdown
from ..data.data import fetch_data

# Fetch the data
data = fetch_data()

# Remove the original website URL column
data = data.drop(columns=['Longitude', 'Latitude'])

data['Website Link'] = data.apply(lambda row: f'<a href="{row["Website"]}">{row["Name"]}</a>', axis=1) # Generate HTML Links

#data = data.drop(columns=['Google Maps Link'])
#data = data.drop(columns=['Website'])

# Define the columns for the table
columns = [
    {"field": "Name", "title": "Name"},
    {"field": "Street", "title": "Street"},
    {"field": "City", "title": "City"},
    {"field": "State", "title": "State / Province"},
    {"field": "Postal Code", "title": "Postal Code"},
    {"field": "Country", "title": "Country"},
    {"field": "Type", "title": "Type"},
    {"field": "Website Link", "title": "Website", "type": "html"},
    {"field": "Website", "title": "Website"},
    {"field": "Google Maps", "title": "Google Maps", "type": "html"},
]

# Create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
