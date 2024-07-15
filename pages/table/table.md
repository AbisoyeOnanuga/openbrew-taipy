# **Breweries List**{: .color-primary}

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

    function renderTable() {
        const tableBody = document.getElementById('table-body');
        tableBody.innerHTML = '';
        const start = (currentPage - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        const paginatedData = data.slice(start, end);

        paginatedData.forEach(row => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${row['Name']}</td>
                <td>${row['Street']}</td>
                <td>${row['City']}</td>
                <td>${row['State']}</td>
                <td>${row['Postal Code']}</td>
                <td>${row['Country']}</td>
                <td>${row['Type']}</td>
                <td>${row['Website Link']}</td>
                <td>${row['Google Maps Link']}</td>
            `;
            tableBody.appendChild(tr);
        });

        document.getElementById('page-info').innerText = `Page ${currentPage} of ${Math.ceil(data.length / rowsPerPage)}`;
    }

    function prevPage() {
        if (currentPage > 1) {
            currentPage--;
            renderTable();
        }
    }

    function nextPage() {
        if (currentPage < Math.ceil(data.length / rowsPerPage)) {
            currentPage++;
            renderTable();
        }
    }

    function updateRowLimit() {
        rowsPerPage = parseInt(document.getElementById('row-limit').value);
        currentPage = 1;
        renderTable();
    }

    document.addEventListener('DOMContentLoaded', () => {
        renderTable();
    });
</script>