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

        .taipy-table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .taipy-table th, .taipy-table td {{
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }}

        .taipy-table th {{
            background-color: rgb(140, 110, 80);
            color: white;
        }}

        .taipy-table tr:nth-child(odd) {{
            background-color: var(--color-background-odd-row);
            color: var(--color-text-odd-row);
        }}

        .taipy-table tr:nth-child(even) {{
            background-color: rgba(200, 180, 140, 0.5);  /* Slightly darker for even rows */
        }}

        .taipy-table tr:hover {{
            background-color: rgba(200, 180, 140, 0.7);  /* Darker background on hover */
        }}

        .pagination-controls {{
            margin-top: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .pagination-controls button, .pagination-controls select {{
            padding: 5px 10px;
            border-radius: var(--border-radius);
            border: 1px solid #ddd;
            background-color: rgb(140, 110, 80);
            color: white;
            cursor: pointer;
        }}

        .pagination-controls button:disabled {{
            background-color: #ccc;
            cursor: not-allowed;
        }}
    </style>
</head>
<body>
    <h1 class="color-primary">Breweries List</h1>
    <table id="brewery-table" class="taipy-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Street</th>
                <th>City</th>
                <th>State / Province</th>
                <th>Postal Code</th>
                <th>Country</th>
                <th>Type</th>
                <th>Website</th>
                <th>Google Maps</th>
            </tr>
        </thead>
        <tbody id="table-body">
            <!-- Rows will be inserted here by JavaScript -->
        </tbody>
    </table>

    <div class="pagination-controls">
        <button id="prev-page" onclick="prevPage()">Previous</button>
        <span id="page-info"></span>
        <button id="next-page" onclick="nextPage()">Next</button>
        <select id="row-limit" onchange="updateRowLimit()">
            <option value="10">10</option>
            <option value="50">50</option>
            <option value="100">100</option>
        </select>
    </div>

    <script>
        let data = {{ data_dict | tojson }};
        let currentPage = 1;
        let rowsPerPage = 10;

        function renderTable() {{
            const tableBody = document.getElementById('table-body');
            tableBody.innerHTML = '';
            const start = (currentPage - 1) * rowsPerPage;
            const end = start + rowsPerPage;
            const paginatedData = data.slice(start, end);

            paginatedData.forEach(row => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${{row['Name']}}</td>
                    <td>${{row['Street']}}</td>
                    <td>${{row['City']}}</td>
                    <td>${{row['State']}}</td>
                    <td>${{row['Postal Code']}}</td>
                    <td>${{row['Country']}}</td>
                    <td>${{row['Type']}}</td>
                    <td>${{row['Website Link']}}</td>
                    <td>${{row['Google Maps Link']}}</td>
                `;
                tableBody.appendChild(tr);
            }});

            document.getElementById('page-info').innerText = `Page ${{currentPage}} of ${{Math.ceil(data.length / rowsPerPage)}}`;
        }}

        function prevPage() {{
            if (currentPage > 1) {{
                currentPage--;
                renderTable();
            }}
        }}

        function nextPage() {{
            if (currentPage < Math.ceil(data.length / rowsPerPage)) {{
                currentPage++;
                renderTable();
            }}
        }}

        function updateRowLimit() {{
            rowsPerPage = parseInt(document.getElementById('row-limit').value);
            currentPage = 1;
            renderTable();
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            renderTable();
        }});
    </script>
</body>
</html>
""")
