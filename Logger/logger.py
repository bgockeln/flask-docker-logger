from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route("/log", methods=["POST"])
def log_entry():
    """
    Handle incoming POST requests to /log.
    Expects JSON data and writes it to logs.txt with a timestamp.
    """

    data = request.json

    # Append log entry with timestamp
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {data}\n")

    # Return HTTP 204 (No Content) to confirm successful logging
    return "", 204

if __name__ == "__main__":
    # Run the Flask app on all interfaces (for Docker accessibility)
    app.run(host="0.0.0.0", port=5001)

