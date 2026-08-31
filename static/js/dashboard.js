document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.analysis-form');
    if (!form) return;

    // Elements to update
    const updateMetrics = (data) => {
        // We assume we have the metric-card elements in DOM, if they exist
        const metricValues = document.querySelectorAll('.metric-value');
        if (metricValues.length === 3 && data.market_data) {
            metricValues[0].textContent = data.market_data.TAM.value;
            metricValues[1].textContent = data.market_data.SAM.value;
            metricValues[2].textContent = data.market_data.SOM.value;
        }

        // Competitor Table
        const tbody = document.querySelector('tbody');
        if (tbody && data.competitors) {
            tbody.innerHTML = '';
            data.competitors.forEach(comp => {
                const badgeClass = comp.type === 'DIRECT' ? 'badge-direct' : 'badge-indirect';
                const row = `
                    <tr>
                        <td style="font-weight: 600; color: #fff;">${comp.name}</td>
                        <td><span class="badge ${badgeClass}">${comp.type}</span></td>
                        <td>${comp.market_share}</td>
                        <td>${comp.revenue}</td>
                        <td class="text-success">${comp.growth}</td>
                    </tr>
                `;
                tbody.insertAdjacentHTML('beforeend', row);
            });
        }
    };

    const fetchAnalytics = async () => {
        const formData = new FormData(form);
        const dataObj = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObj)
            });

            if (response.ok) {
                const result = await response.json();
                updateMetrics(result);
            }
        } catch (err) {
            console.error("Failed to fetch dynamic data:", err);
        }
    };

    // Attach listeners to all inputs and selects
    const inputs = form.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            // Only update if we already have the results grid showing
            const resultsGrid = document.querySelector('.results-grid');
            if (resultsGrid) {
                fetchAnalytics();
            }
        });
    });
});
