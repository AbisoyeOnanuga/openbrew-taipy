from taipy.gui import Html
from ..data.data import fetch_data

data = fetch_data()

# Your logic to drop columns and manipulate data
data = data.drop(columns=['Longitude', 'Latitude', 'Website'])
#data = data.drop(columns=['Google Maps Link'])

table_rows = ''.join([f"<tr><td>{row['Name']}</td><td>{row['Street']}</td><td>{row['City']}</td><td>{row['State']}</td><td>{row['Postal Code']}</td><td>{row['Country']}</td><td>{row['Type']}</td><td>{row['Google Maps']}</td><td>{row['Website Link']}</td></tr>" for index, row in data.iterrows()])
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
