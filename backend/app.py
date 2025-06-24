from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import psutil
import os



app = Flask(__name__)
CORS(app)  # permite conexión desde cualquier origen (tu HTML local)

@app.route("/api/metrics")
def metrics():

# optener la info de todo lo psible para detalles del hardwar wtc
    name = psutil.net_if_addrs()
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net = psutil.net_io_counters()
    return jsonify({
        "name":name,
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "net_sent": round(net.bytes_sent / (1024 * 1024), 2),
        "net_recv": round(net.bytes_recv / (1024 * 1024), 2)
    })

# Servir archivos estáticos (index.html, js.js, styles.css, etc.)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@app.route("/")
def root():
    return send_from_directory(BASE_DIR, "index.html")

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# crear mi propia api de lectura sin dependencias

# Pendiente