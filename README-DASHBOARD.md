# Dashboard Guide
## Overview
The dashboard.py file handles the dashboard view of the Brewery Data Exploration app. It provides an interactive interface for analyzing brewery data, allowing users to select a brewery and view detailed information.

## Code Explanation
### dashboard.py
```python
    from taipy.gui import Markdown, State
    import pandas as pd

    from ..data.data import fetch_data

    data = fetch_data()

    # Initialize the selected brewery name
    selected_brewery = data.iloc[0]['Name']
    data_brewery = None

    def initialize_brewery_data(data, selected_brewery):
        # Filter the data for the selected brewery
        data_brewery = data.loc[data['Name'] == selected_brewery]
        return data_brewery

    data_brewery = initialize_brewery_data(data, selected_brewery)

    def on_change_brewery(state: State):
        # Update data_brewery with the selected brewery
        state.data_brewery = initialize_brewery_data(data, state.selected_brewery)

    # List of brewery names for the selector
    selector_brewery = list(data['Name'].unique())

    dashboard_md = Markdown("pages/dashboard/dashboard.md")
```
- Data Initialization: Fetches the brewery data using the fetch_data function from the data module.
- Selected Brewery: Initializes the selected brewery name and filters the data for the selected brewery.
- on_change_brewery Function: Updates the data for the selected brewery when the user changes the selection.
- Markdown Content: Defines the dashboard page content using a Markdown file.

### dashboard.md
The dashboard.md file contains the Markdown content for the dashboard page.
```markdown
    # **Brewery Dashboard**{: .color-primary} Information

    <|{selected_brewery}|selector|lov={selector_brewery}|on_change=on_change_brewery|dropdown|label=Brewery Name|>

    <br/>

    <|layout|columns=1 1 1|gap=50px|
    <|card|
    **Brewery Name**{: .color-primary}
    <|{data_brewery.iloc[0]['Name']}|text|class_name=h2|>
    |>

    <|card|
    **Brewery Type**{: .color-primary}
    <|{data_brewery.iloc[0]['Type']}|text|class_name=h2|>
    |>

    <|card|
    **Location**{: .color-primary}
    <|{data_brewery.iloc[0]['Street']}, {data_brewery.iloc[0]['City']}, {data_brewery.iloc[0]['State']}|text|class_name=h2|>
    |>
    |>

    <br/>
    <br/>

    <|layout|columns=1 1 1|gap=50px|
    <|card|
    **Contact**{: .color-primary}
    <|{data_brewery.iloc[0]['Phone']}|text|class_name=h2|>
    |>

    <|card|
    **Google Maps**{: .color-primary}
    <|{data_brewery.iloc[0]['Google Maps']}|text|class_name=h2|>
    |>

    <|card|
    **Website**{: .color-primary}
    <|{data_brewery.iloc[0]['Website']}|text|class_name=h2|>
    |>
    |>
```
- Selector: Allows users to select a brewery from a dropdown list.
- Cards Layout: Displays detailed information about the selected brewery in a card layout, including name, type, location, contact information, Google Maps link, and website.
