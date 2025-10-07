// Funciones para renderizar gráficos del dashboard
function renderTrendChart(canvasId, labels, ingresos, egresos){
	const ctx = document.getElementById(canvasId);
	if(!ctx) return;
	new Chart(ctx, {
		type: 'bar',
		data: {
			labels: labels,
			datasets: [
				{ label: 'Ingresos', data: ingresos, backgroundColor: '#F49E0C' },
				{ label: 'Egresos', data: egresos, backgroundColor: '#101827' }
			]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
			animation: { duration: 0 },
			plugins: { legend: { position: 'top' } }
		}
	});
}

function renderDonutChart(canvasId, data, labels){
	const ctx = document.getElementById(canvasId);
	if(!ctx) return;
	new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: labels,
			datasets: [{ data: data, backgroundColor: ['#111827', '#f6c85f', '#f59e0b'] }]
		},
		options: { responsive: true, maintainAspectRatio: false, animation: { duration: 0 }, plugins: { legend: { position: 'bottom' } } }
	});
}

// Placeholder: dashboard scripts removed. Regenerar si se necesitan gráficos dinámicos.
