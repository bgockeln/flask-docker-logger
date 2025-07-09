from flask import Flask, request
# Flask Komponenten:
# Flask: erstellt die Webanwendung.
# request: enthält Informationen zur aktuellen Anfrage (IP in diesem Fall).

import datetime
# Für Zeistempel beim schreiben der Log-Einträge.

app = Flask(__name__)
# Erstellt die Flask App.
# (__name__) ist der Name des aktuellen Moduls.

@app.route("/log", methods=["POST"])
# Route für "/log", akzeptiert nur POST-Anfragen

def log_entry():
    data = request.json
    # Holt die gesendeten JSON-Daten aus der Anfrage.

    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {data}\n")
        # Öffnet und oder erstellt die Datei logs.txt in Anfügemodus.
        # Schreibt aktuellen Zeitstempel und die empfangenen Daten in eine neue Zeile.

    return "", 204
    # Antwortet mit HTTP-Status 204(No Content). Alles ok aber keine Daten zurück.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    # Startet die Flask-App auf allen Netzwerkinterfaces (0.0.0.0) und Port 5001.
