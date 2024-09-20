from flask import Flask, render_template, jsonify
import psutil

# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to get system data (already working)
@app.route('/api/data')
def get_system_data():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return jsonify({'cpu_usage': cpu_usage, 'memory_usage': memory_usage})

@app.route('/api/processes')
def get_top_processes():
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            proc_info = proc.info
            proc_info['memory_percent'] = round(proc.memory_percent(), 2)  # Use psutil's memory_percent method
            processes.append(proc_info)
        except psutil.NoSuchProcess:
            pass
    
    # Sort by CPU usage and limit to top 5 processes
    top_cpu_processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)[:5]
    
    return jsonify(top_cpu_processes)

if __name__ == '__main__':
    app.run(debug=True)
