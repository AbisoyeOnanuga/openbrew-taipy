# Brewery Data Exploration with Taipy
## Overview
This project demonstrates how to build a multipage web application using Taipy to explore data from the Open Brewery DB API at <a href="https://openbrewerydb.org">Open Brewery DB</a>. The app includes a list view, a dashboard, and a map view, all styled with custom CSS and Taipy’s Stylekit.

## Table of Contents
1. Setup Instructions
2. Application Structure
    - main.py
    - data.py
    - table.py
    - dashboard.py
    - map.py
    - style.css
    - root.py
3. Detailed Component Guides

## Setup Instructions

### Prerequisites
- Python 3.x
- Taipy library
- Pandas
- Requests

### Installation
1. Clone the repository:
```bash
    git clone <repository-url>
    cd <repository-directory>
```

2. Install the required libraries:
`pip install taipy pandas requests`

## Application Structure
### main.py
This is the main entry point of the application. It sets up the pages and the stylekit.

## Features

- **Table Page**: A comprehensive table listing all the breweries with sortable columns.
- **Dashboard Page**: Visual analytics of brewery data including charts and graphs.
- **Map Page**: An interactive map displaying the geographical distribution of breweries.

## Getting Started

To get started with OpenBrew-Taipy, clone this repository and install the required dependencies.

```bash
git clone https://github.com/your-username/openbrew-taipy.git
cd openbrew-taipy
pip install -r requirements.txt
```

## Detailed Component Guides
For detailed guides on each component, refer to the following links:

- [**Style Guide**](./README-STYLE.md): Information for stylekit and custom CSS.
- [**Root Guide**](./README-ROOT.md): Detailed guide for root.py and root.md.
- [**Data Guide**](./README-DATA.md): Detailed instructions for data.
- [**Table Guide**](./README-TABLE.md): Information for table.
- [**Dashbaord Guide**](./README-DASHBOARD.md): The dashboard.
- [**Map Guide**](./README-MAP.md): Detailed instructions for map.
