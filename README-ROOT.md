# Root Guide
## Overview
The `root.py` file sets up the root page of the Brewery Data Exploration app. It initializes the data and defines the main Markdown content for the root page.

## Code Explanation
### root.py
```Python
    from taipy.gui import Markdown
    import numpy as np
    from .data.data import fetch_data

    data = fetch_data()

    selector_location = list(np.sort(data['Name'].astype(str).unique()))
    selected_location  = '(405) Brewing Co'

    root = Markdown("pages/root.md")
```

- Data Initialization: Fetches the brewery data using the fetch_data function from the data module.
- Selector Location: Creates a sorted list of brewery names for use in the application.
- Markdown Content: Defines the root page content using a Markdown file.

### root.md
The `root.md` file contains the HTML and Markdown content for the root page.

```html
    <h1 style="vertical-align: middle; font-size: 75px; display: flex; justify-content: center; align-items: center; margin-;">
        <img style="vertical-align: middle; margin-right: 20px;" src="./image/openbrew-taipy-logo.png" width="200" height="200" />
        Openbrew Taipy
    </h1>
    <|toggle|theme|>
    <center><|navbar|></center>
```

- Header: Displays the application title and logo.
- Theme Toggle: Adds a theme toggle switch for light and dark modes.
- Navbar: Centers the navigation bar.