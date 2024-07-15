import pandas as pd
from taipy.gui import Markdown
from ..data.data import fetch_data
from taipy.gui import Gui
# Fetch the data
data = fetch_data()

# Print the columns to check if 'Website' is present
print(data.columns)

# Fetch the data
data = fetch_data()

# Add an ID column for easier selection in JavaScript
data['id'] = data.index

# Convert the DataFrame to a dictionary for JavaScript
data_dict = data.to_dict(orient='records')

# Assuming 'Website' and 'Google Maps' columns contain the URLs
if 'Website' in data.columns:
    # Create the Website and Google Maps links using HTML syntax
    data['Website Link'] = data.apply(lambda row: f'<a href="{row["Website"]}" target="_blank">{row["Name"]}</a>', axis=1)
    data['Google Maps Link'] = data.apply(lambda row: f'<a href="{row["Google Maps"]}" target="_blank">Google Maps</a>', axis=1)
# Remove the original website URL column

data = data.drop(columns=['Longitude', 'Latitude', 'Website', 'Google Maps'])

# Convert the DataFrame to a dictionary for JavaScript
data_dict = data.to_dict(orient='records')

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
    {"field": "Google Maps Link", "title": "Google Maps", "type": "html"},
    {"field": "Website", "title": "Website", "type": "html", "class": lambda row: f'website-{row["id"]}'},
    {"field": "Google Maps", "title": "Google Maps", "type": "html", "class": lambda row: f'maps-{row["id"]}'},
]

# Create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
