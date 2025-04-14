// Simulación de datos aleatorios
function getRandom(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// Actualizar métricas simuladas en el DOM
function actualizarMetricas() {
  document.getElementById('cpu').textContent = getRandom(15, 80) + '%';
  document.getElementById('ram').textContent = getRandom(30, 95) + '%';
  document.getElementById('disk').textContent = getRandom(40, 90) + '%';
  document.getElementById('net').textContent = getRandom(5, 100) + ' Mbps';
  document.getElementById('logs').textContent = `# Procesos activos:\nPID 2345 - node\nPID 1182 - python3\nPID 991 - nginx\nPID 881 - systemd`;
}

// Llamar a la función cada 2 segundos
setInterval(actualizarMetricas, 2000);

// =====================
// Gráfico de carga (Chart.js)


// =====================
const ctx = document.getElementById('chart').getContext('2d');
const chartData = {
  labels: [],
  datasets: [{
    label: 'Carga del sistema',
    backgroundColor: '#3c8bf0',
    borderColor: '#3c8bf0',
    data: [],
    tension: 0.3,
    fill: false
  }]
};

const chart = new Chart(ctx, {
  type: 'line',
  data: chartData,
  options: {
    scales: {
      y: {
        beginAtZero: true,
        max: 100
      }
    }
  }
});

// Simulación de datos en gráfico
setInterval(() => {
  const now = new Date();
  const tiempo = now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds();
  const carga = getRandom(10, 90);

  if (chartData.labels.length > 10) {
    chartData.labels.shift();
    chartData.datasets[0].data.shift();
  }

  chartData.labels.push(tiempo);
  chartData.datasets[0].data.push(carga);
  chart.update();
}, 3000);
