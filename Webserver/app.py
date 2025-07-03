import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-ip")
def get_ip():
    ip = request.remote_addr
    try:
        requests.post("http://logger:5001/log", json={"ip": ip, "route": "/get-ip"})
    except Exception as e:
        print("Logging failed:", e)
    return jsonify({"ip": ip})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
