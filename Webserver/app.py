# Zum senden von HTTP Anfragen
import requests

from flask import Flask, jsonify, render_template, request
# Flask Komponenten:
# Flask: erstellt die Webanwendung
# jsonify: konvertiert Python-Daten in JSON-Antworten
# render_template: rendert meine HTLM-Datei aus dem template_folder
# request: enthält Informationen zur aktuellen Anfrage. (IP in diesem Fall)

app = Flask(__name__, template_folder='templates', static_folder='static')
# Erstellt die Flask App
# __name__: Name des aktuellen Moduls
# template_folder: Ordner für HTLM Vorlagen (Flask Standart)
# static_folder: Order für statische Dateien wie Css (Flask Standart)

@app.route("/")
    # Route für die Startseite "/"
def index():
    return render_template("index.html")
    # Gibt die index.html aus dem template_folder zurück

@app.route("/get-ip")
def get_ip():
    # Route für "/get-ip", gibt die IP des Nutzers zurück
    ip = request.remote_addr
    # Holt die IP des Anfragenden

    try:
        requests.post("http://logger:5001/log", json={"ip": ip, "route": "/get-ip"})
        # Versucht die IP und Route an den Logger-Service zu schicken
        # logger ist hier der Name des Docker-Containers mit dem Logging-Service

    except Exception as e:
        print("Logging failed:", e)
        # Falls das Senden der Log-Daten fehlschägt, wird eine Fehlermeldung ausgegeben
        # Die Anwendung läuft trotzdem weiter ohne Fehler
    
    return jsonify({"ip": ip})
    #Gib die IP als JSON-Antwort zurück

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # Starte den Flask-Server, erreichbar auf allen Netzwerkinterfaces (0.0.0.0) 
    # und dem Port 5000
