async function obtenerDatosSistema() {
  try {
    const res = await fetch("http://localhost:5000/api/metrics");
    const data = await res.json();

    document.getElementById('cpu').textContent = data.cpu + '%';
    document.getElementById('ram').textContent = data.ram + '%';
    document.getElementById('disk').textContent = data.disk + '%';
    document.getElementById('net').textContent = `↗ ${data.net_sent} MB / ↘ ${data.net_recv} MB`;

    actualizarGrafico(data.cpu); // Opcional: si tienes el gráfico
  } catch (error) {
    console.error("Error al obtener métricas:", error);
  }
}

setInterval(obtenerDatosSistema, 3000); // Llamar cada 3 segundos
