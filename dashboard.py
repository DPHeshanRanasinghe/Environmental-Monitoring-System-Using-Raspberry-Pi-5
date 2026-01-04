# dashboard.py - Simple Flask web server to display the chart

from flask import Flask, render_template_string, send_file
import time
import os

app = Flask(__name__)

# --- HTML TEMPLATE ---
# The HTML contains CSS for a clean look and a meta tag for auto-refresh
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pi 5 Environmental Monitor</title>
    <meta http-equiv="refresh" content="60"> <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
        h1 { color: #007bff; }
        .container { 
            background-color: white; 
            padding: 20px; 
            border-radius: 8px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
            display: inline-block;
        }
        img { 
            max-width: 100%; 
            height: auto; 
            border: 1px solid #ddd; 
            padding: 5px; 
            background-color: #fff;
            margin-top: 15px;
        }
        p { color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Local Environmental Heartbeat (Colombo, LK)</h1>
        <p>Data last updated: {{ last_updated }}</p>
        <img src="/chart" alt="Temperature Trend Chart">
        <p>Powered by Raspberry Pi 5 and Python Flask</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Renders the main dashboard page."""
    
    # Check the file's modification time for the 'last updated' timestamp
    if os.path.exists('temperature_chart.png'):
        timestamp = os.path.getmtime('temperature_chart.png')
        last_updated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    else:
        last_updated = "Chart not found. Please run analyzer.py."

    return render_template_string(HTML_TEMPLATE, last_updated=last_updated)

@app.route('/chart')
def get_chart():
    """Serves the actual chart image file to the browser."""
    
    if os.path.exists('temperature_chart.png'):
        # send_file is used to send binary data (like an image)
        return send_file('temperature_chart.png', mimetype='image/png')
    else:
        return "Chart not found", 404

if __name__ == '__main__':
    # Running on '0.0.0.0' makes the server accessible from your laptop's network
    print("\n--- Starting Flask Web Server ---")
    print("Accessible via: http://[Your.Pi.IP.Address]:5000")
    print("Press CTRL+C to stop the server.")
    
    # 'debug=True' is helpful for development, but remove for a long-running service
    app.run(host='0.0.0.0', port=5000, debug=True)
