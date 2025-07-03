from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_entry():
    data = request.json
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {data}\n")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

