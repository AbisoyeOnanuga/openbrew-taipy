import pandas as pd
from taipy.gui import Markdown
from ..data.data import fetch_data

# Fetch the data
data = fetch_data()

# We need to add Google Maps and website links to the data
data['Google Maps Link'] = data.apply(lambda row: "Google Maps Link: https://www.google.com/maps/search/?api=1&query=" + str(row['Latitude']) + "," + str(row['Longitude']), axis=1)
data['Website Link'] = data.apply(lambda row: f"[{row['Name']} Website]({row['Website']})" if row['Website'] else "No Website", axis=1)

# Create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
