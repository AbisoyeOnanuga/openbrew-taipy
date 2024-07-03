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
