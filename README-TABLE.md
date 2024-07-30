# Table Guide
## Overview
The table.py file handles the table view of the Brewery Data Exploration app. It displays a comprehensive list of breweries with various details.

## Code Explanation
### table.py
```python
    import pandas as pd
    from taipy.gui import Markdown
    from ..data.data import fetch_data
    from taipy.gui import Gui

    # Fetch the data
    data = fetch_data()

    # Print the columns to check if 'Website' is present
    print(data.columns)

    # Convert the DataFrame to a dictionary for JavaScript
    data_dict = data.to_dict(orient='records')

    # Assuming 'Website' and 'Google Maps' columns contain the URLs
    if 'Website' in data.columns:
        # Create the Website and Google Maps links using HTML syntax
        data['Website Link'] = data.apply(lambda row: f'<a href="{row["Website"]}" target="_blank">{row["Name"]}</a>', axis=1)
        data['Google Maps Link'] = data.apply(lambda row: f'<a href="{row["Google Maps"]}" target="_blank">Google Maps</a>', axis=1)

    # Remove the original website URL column
    data = data.drop(columns=['Longitude', 'Latitude', 'Google Maps Link', 'Website Link'])

    # Define the columns for the table
    columns = [
        {"field": "Name", "title": "Name"},
        {"field": "Street", "title": "Street"},
        {"field": "City", "title": "City"},
        {"field": "State", "title": "State / Province"},
        {"field": "Postal Code", "title": "Postal Code"},
        {"field": "Country", "title": "Country"},
        {"field": "Type", "title": "Type"},
        {"field": "Website", "title": "Website", "type": "html"},
        {"field": "Google Maps", "title": "Google Maps", "type": "html"}
    ]

    # Create a Markdown control and set the content to the Taipy table syntax
    table_md = Markdown("pages/table/table.md")
```

## Markdown for Table View
```markdown
    # **Breweries List**{: .color-primary}

    <|{data}|table|columns=columns|page_size=10|page_size_options=[10, 50, 100]|filter=True|>
```
