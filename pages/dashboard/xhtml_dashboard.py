from taipy.gui import Html, State
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


# Add Google Maps and Website links using HTML syntax
data['Google Maps Link'] = data.apply(lambda row: f"<a href='https://www.google.com/maps/search/?api=1&query={row['Latitude']},{row['Longitude']}' target='_blank'>View Map</a>", axis=1)
data['Website Link'] = data.apply(lambda row: f"<a href='{row['Website']}' target='_blank'>{row['Name']} Website</a>" if row['Website'] else "No Website", axis=1)

# Generate options for the selector
options = '\n'.join([f'<option value="{name}">{name}</option>' for name in selector_brewery])

import json

# Convert the data DataFrame to a JSON string
data_json = json.dumps(data.to_dict(orient='records'))

# Define the XHTML dashboard
dashboard = Html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {{
            --border-radius-small: calc(var(--border-radius) / 2);
            --border-radius-large: calc(var(--border-radius) * 2);
            --box-shadow: 5px 5px 15px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
            --border-radius: 10px;
            --color-background-odd-row: #f2f2f2; /* Light grey for odd row background */
            --color-text-odd-row: #333333; /* Dark grey for odd row text */
        }}

        .card-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* 3 columns grid */
            gap: 20px; /* Adjust spacing between cards */
        }}

        .card {{
            background: rgba(140, 110, 80, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(140, 110, 80, 0.5);
            border-radius: var(--border-radius-large);
            padding: 20px;
            /* Add other card styles as needed */
        }}

        .card:hover {{
            background: rgba(200, 180, 140, 0.5);
            border: 1px solid rgba(140, 110, 80, 0.8);
        }}

        /* Additional styles for light mode (if needed) */
        @media (prefers-color-scheme: light) {{
            .card {{
                background: rgba(200, 180, 140, 0.2);
                border: 1px solid rgba(200, 180, 140, 0.5);
            }}
            /* ... other light mode styles ... */
        }}
    </style>
</head>
<body>
    <h1 class="color-primary">Brewery Dashboard</h1>
    <label for="brewery-selector">Brewery Name:</label>
    <select id="brewery-selector" onchange="onChangeBrewery()">
        {''.join([f'<option value="{brewery}">{brewery}</option>' for brewery in selector_brewery])}
    </select>

    <div id="brewery-info" class="card-container">
        <div class="card">
            <h2 class="color-primary">Brewery Name</h2>
            <p class="h2">{data_brewery.iloc[0]['Name']}</p>
        </div>
        <div class="card">
            <h2 class="color-primary">Brewery Type</h2>
            <p class="h2">{data_brewery.iloc[0]['Type']}</p>
        </div>
        <div class="card">
            <h2 class="color-primary">Location</h2>
            <p class="h2">{data_brewery.iloc[0]['Street']}, {data_brewery.iloc[0]['City']}, {data_brewery.iloc[0]['State']}</p>
        </div>
        <div class="card">
            <h2 class="color-primary">Contact</h2>
            <p class="h2">{data_brewery.iloc[0]['Phone']}</p>
        </div>
        <div class="card">
            <h2 class="color-primary">Google Maps</h2>
            <p class="h2">{data_brewery.iloc[0]['Google Maps Link']}</p>
        </div>
        <div class="card">
            <h2 class="color-primary">Website</h2>
            <p class="h2">{data_brewery.iloc[0]['Website Link']}</p>
        </div>
    </div>

    <script>
        let data = {data_dict};
        let selectedBrewery = "{selected_brewery}";

        function onChangeBrewery() {
            const selector = document.getElementById('brewery-selector');
            selectedBrewery = selector.value;
            updateBreweryInfo();
        }

        function updateBreweryInfo() {
            const brewery = data.find(b => b.Name === selectedBrewery);
            document.querySelector('#brewery-info .card:nth-child(1) .h2').innerText = brewery.Name;
            document.querySelector('#brewery-info .card:nth-child(2) .h2').innerText = brewery.Type;
            document.querySelector('#brewery-info .card:nth-child(3) .h2').innerText = `${brewery.Street}, ${brewery.City}, ${brewery.State}`;
            document.querySelector('#brewery-info .card:nth-child(4) .h2').innerText = brewery.Phone;
            document.querySelector('#brewery-info .card:nth-child(5) .h2').innerHTML = brewery['Google Maps Link'];
            document.querySelector('#brewery-info .card:nth-child(6) .h2').innerHTML = brewery['Website Link'];
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateBreweryInfo();
        });
    </script>
</body>
</html>
""")
