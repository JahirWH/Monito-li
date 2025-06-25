from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import time
import subprocess
import platform

app = Flask(__name__)
CORS(app) 

def get_cpu_usage():
    try:
        with open('/proc/stat', 'r') as f:
            line1 = f.readline()
        time.sleep(0.1)
        with open('/proc/stat', 'r') as f:
            line2 = f.readline()
        cpu1 = [int(x) for x in line1.split()[1:]]
        cpu2 = [int(x) for x in line2.split()[1:]]
        idle1, idle2 = cpu1[3], cpu2[3]
        total1, total2 = sum(cpu1), sum(cpu2)
        idle_delta = idle2 - idle1
        total_delta = total2 - total1
        if total_delta == 0:
            return 0
        return round((1 - idle_delta / total_delta) * 100, 2)
    except Exception as e:
        print(f"Error en get_cpu_usage: {e}")
        return 0

def get_memory_usage():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
        total = available = None
        for line in lines:
            if line.startswith('MemTotal:'):
                total = int(line.split()[1])
            elif line.startswith('MemAvailable:'):
                available = int(line.split()[1])
        if total and available:
            used = total - available
            return round((used / total) * 100, 2)
    except:
        pass
    return 0
    
def get_disk_usage():
    try:
        st = os.statvfs('/')
        total = st.f_blocks * st.f_frsize
        free = st.f_bfree * st.f_frsize
        used = total - free
        return round((used / total) * 100, 2)
    except Exception as e:
        print(f"Error en get_disk_usage: {e}")
        return 0

def get_network_stats():
    """Obtiene estadísticas de red leyendo /proc/net/dev"""
    try:
        with open('/proc/net/dev', 'r') as f:
            lines = f.readlines()
        total_sent = 0
        total_recv = 0
        for line in lines[2:]:  # Ignora las primeras 2 líneas
            parts = line.split()
            if len(parts) >= 10:
                interface = parts[0].split(':')[0]
                if interface != 'lo':
                    total_recv += int(parts[1])
                    total_sent += int(parts[9])
        return {
            'sent': round(total_sent / (1024 * 1024), 2),
            'recv': round(total_recv / (1024 * 1024), 2)
        }
    except:
        return {'sent': 0, 'recv': 0}

@app.route("/api/metrics")
def metrics():
    # Obtener métricas usando solo módulos integrados de Python
    cpu = get_cpu_usage()
    ram = get_memory_usage()
    disk = get_disk_usage()
    net = get_network_stats()
    
    return jsonify({
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "net_sent": net['sent'],
        "net_recv": net['recv']
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

