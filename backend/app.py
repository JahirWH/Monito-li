from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)  # permite conexión desde cualquier origen (tu HTML local)

@app.route("/api/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net = psutil.net_io_counters()
    return jsonify({
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "net_sent": round(net.bytes_sent / (1024 * 1024), 2),
        "net_recv": round(net.bytes_recv / (1024 * 1024), 2)
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
