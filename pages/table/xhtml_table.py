from taipy.gui import Html
from ..data.data import fetch_data

data = fetch_data()

# Your logic to drop columns and manipulate data
# Generate HTML Links
data['Google Maps'] = data.apply(lambda row: f"<a href='https://www.google.com/maps/search/?api=1&query={row['Latitude']},{row['Longitude']}' target='_blank'>View Map</a>", axis=1)
data['Website Link'] = data.apply(lambda row: f"<a href='{row['Website']}' target='_blank'>{row['Name']} Website</a>" if row['Website'] else "No Website", axis=1)
data = data.drop(columns=['Longitude', 'Latitude', 'Website'])
#data = data.drop(columns=['Google Maps Link'])

table_rows = ''.join([f"<tr><td>{row['Name']}</td><td>{row['Street']}</td><td>{row['City']}</td><td>{row['State']}</td><td>{row['Postal Code']}</td><td>{row['Country']}</td><td>{row['Type']}</td><td>{row['Website Link']}</td><td>{row['Google Maps Link']}</td></tr>" for index, row in data.iterrows()])
table_html = f"<table>{table_rows}</table>"

# Define the XHTML page
table = Html(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Brewery Directory</title>
</head>
<body>
    <h1>US Brewery Directory</h1>
    {table_html}
</body>
</html>
""")
