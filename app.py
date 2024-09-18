from flask import Flask, render_template, jsonify
import psutil

# Initialize app
app = Flask(__name__)

# Route to serve the main and only HTML page
@app.route('/')
def index():
    return render_template('index.html')  # 'index.html' is in the 'templates' folder

# API to get system usage data (Total CPU usage, no per-core breakdown)
@app.route('/api/data')
def get_system_data():
    # Get total CPU usage across all cores
    total_cpu_usage = psutil.cpu_percent(interval=1, percpu=False)

    # Get memory usage
    memory_usage = psutil.virtual_memory().percent

    return jsonify({
        'cpu_usage': total_cpu_usage,  # Total CPU usage (across all cores)
        'memory_usage': memory_usage,  # Memory usage
    })

if __name__ == '__main__':
    app.run(debug=True)
