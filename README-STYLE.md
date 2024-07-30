# Style Guide
## Overview
The style.css file defines the custom CSS styles used in the Brewery Data Exploration app. It includes styles for both light and dark modes, ensuring a cohesive and visually appealing user interface.

## CSS Variables
The CSS variables are defined in the :root selector to ensure they are accessible throughout the stylesheet.

```css
    :root {
        --border-radius-small: calc(var(--border-radius) / 2);
        --border-radius-large: calc(var(--border-radius) * 2);
        --box-shadow: 5px 5px 15px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
        --border-radius: 10px;
        --color-background-odd-row: #f2f2f2; /* Light grey for odd row background */
        --color-text-odd-row: #333333; /* Dark grey for odd row text */
    }
```

## Table Styles
Styles for the table rows, including alternating row colors for better readability.

```CSS

    .taipy-table tr:nth-child(odd) {
        color: var(--color-text-odd-row); /* Use a variable for odd row text */
    }
```
### Card Styles
Styles for the brewery-themed cards, including background color, border, and hover effects.

```CSS
    .card {
        background: rgba(140, 110, 80, 0.1);  /* Semi-transparent brown */
        backdrop-filter: blur(10px);  /* Blur effect for the background */
        border: 1px solid rgba(140, 110, 80, 0.5);  /* Thin border matching primary color */
        border-radius: var(--border-radius-large);  /* Rounded corners for a friendly feel */
        overflow: auto;
        /* ... other styles ... */
    }
```

## Light and Dark Mode Styles
Styles for both light and dark modes to ensure the app looks good in different themes.

### Light Mode
```CSS
    @media (prefers-color-scheme: light) {
        .card {
            background: rgba(200, 180, 140, 0.2);  /* Semi-transparent background for the card in light mode */
            border: 1px solid rgba(200, 180, 140, 0.5);
        }
        .card:hover {
            background: rgba(200, 180, 140, 0.5);  /* Darker background on hover */
            border: 1px solid rgba(140, 110, 80, 0.8);
        }
        .taipy-table tr:nth-child(even) {
            background-color: rgba(200, 180, 140, 0.5);  /* Slightly darker for even rows */
        }
        /* ... other light mode styles ... */
    }
```

### Dark Mode
```CSS
    @media (prefers-color-scheme: dark) {
        .taipy-table tr:nth-child(odd) {
            background-color: rgb(75, 65, 55);  /* Dark brown for odd rows */
            color: rgb(255, 235, 205);  /* Cream color for text to ensure visibility */
        }
        .taipy-table tr:nth-child(even) {
            background-color: rgba(50, 40, 30, 0.5);  /* Even darker brown for even rows */
            color: rgb(255, 235, 205);  /* Cream color for text */
        }
        /* ... other dark mode styles ... */
    }
```

## Stylekit in main.py
The `stylekit` dictionary in `main.py` defines the color scheme and typography for the app.
```python
    stylekit = {
        "color_primary": "rgb(140, 110, 80)",  # A rich brown color reminiscent of beer
        "color_secondary": "rgb(200, 180, 140)",  # A lighter complementary color
        "color_background_light": "rgb(255, 248, 240)",  # A warm light background for the light theme
        "color_background_dark": "rgb(50, 40, 30)",  # Dark brown for dark theme background
        "color_paper_dark": "rgb(75, 65, 55)",  # Darker brown for elevated elements in dark theme
        "color_paper_light": "rgb(255, 255, 255)",  # White for elevated elements in light theme
        "color-contrast-dark": "rgb(255, 235, 205)",  # Cream color for contrasting elements on dark backgrounds
        "color-contrast-light": "rgb(50, 40, 30)",  # Dark brown for contrasting elements on light backgrounds
        "color_background_odd_row": "#f2f2f2",  # Light grey for odd row background
        "color_text_odd_row": "#333333",  # Dark grey for odd row text
        "font_family": "'Georgia', serif",  # A font that gives a classic feel
        # ... other style properties ...
    }
```
