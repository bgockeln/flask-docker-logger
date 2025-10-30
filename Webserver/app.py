import requests
from flask import Flask, jsonify, render_template, request

# Simple Flask app that shows user's IP and logs it to the logger service
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")

def index():
    """Serve the main page."""
    return render_template("index.html")

@app.route("/get-ip")
def get_ip():
    """
    Return the client's IP as JSON and send it to the logging service.
    """
    ip = request.remote_addr

    # Send IP and route info to the logger container
    try:
        requests.post("http://logger:5001/log", json={"ip": ip, "route": "/get-ip"})
    except Exception as e:
        print("Logging failed:", e) # Don't fail the app if logger is unreachable
    
    return jsonify({"ip": ip})

if __name__ == "__main__":
    # Run the Flask app on all interfaces for Docker networking
    app.run(host="0.0.0.0", port=5000)

