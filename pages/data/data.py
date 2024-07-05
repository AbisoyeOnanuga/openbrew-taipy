import requests
import pandas as pd

def fetch_data():
    # Define the base URL of the API
    base_url = 'https://api.openbrewerydb.org/v1/breweries?by_country=united%20states'

    # Make a GET request to the API
    response = requests.get(base_url)
    # Parse the response as a JSON object
    breweries = response.json()

    # Convert the list of data to a pandas DataFrame
    data = pd.DataFrame(breweries)
    
    # Select only the desired columns
    data = data[['name', 'brewery_type', 'street', 'city', 'state', 'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url']]

    # Rename the columns to make them more readable
    data.columns = ['Name', 'Type', 'Street', 'City', 'State', 'Postal Code', 'Country', 'Longitude', 'Latitude', 'Phone', 'Website']

    # Add Google Maps and website links to the data with HTML syntax
    data['Google Maps Link'] = data.apply(lambda row: "https://www.google.com/maps/search/?api=1&query=" + str(row['Latitude']) + "," + str(row['Longitude']), axis=1)

    # Add Google Maps and website links to the data with Markdown syntax
    #data['Website Link'] = data.apply(lambda row: f"[{row['Name']} Website]({row['Website']})" if row['Website'] else "No Website", axis=1)
    #data['Google Maps'] = data.apply(lambda row: f"<a href='https://www.google.com/maps/search/?api=1&query={row['Latitude']},{row['Longitude']}' target='_blank'>View Map</a>", axis=1)
    #data['Website Link'] = data.apply(lambda row: f"<a href='{row['Website']}' target='_blank'>{row['Name']} Website</a>" if row['Website'] else "No Website", axis=1)
    
    return data

def prepare_map_data(data):
    # Define a fixed size for the bubbles as there is no size data
    data["size"] = 10  # Fixed size for all bubbles
    # Map 'Type' to colors

    # Create hover text for the bubbles
    data["text"] = data.apply(lambda row:   f"Name: {row['Name']}<br>"
                                            f"Type: {row['Type']}<br>"
                                            f"Address: {row['Street']}, {row['City']}, {row['State']}<br>"
                                            f"Phone: {row['Phone']}<br>"
                                            f"Website: {row['Website']}", axis=1)
    
    # Convert 'Latitude' and 'Longitude' to numeric and drop NaN values
    data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
    data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
    data.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    brewery_type_colors = {
        "micro": "#6f4e37",  # Brown color for most craft breweries
        "nano": "#c8b560",  # Gold color for extremely small breweries
        "regional": "#add8e6",  # Blue color for regional locations
        "brewpub": "#ff4500",  # Orange color for brewpubs
        "large": "#8A2BE2",  # Grey color (deprecated)
        "planning": "#008000",  # Green color for breweries in planning
        "bar": "#808080",  # Grey color (deprecated)
        "contract": "#800080",  # Purple color for contract breweries
        "proprietor": "#ffa500",  # Orange color for proprietor breweries
        "closed": "#ff0000",  # Red color for closed locations
    }
    data["color"] = data["Type"].map(brewery_type_colors)

    return data
