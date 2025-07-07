FROM python:3.12-slim
# Benutzt ein Python-Image(Version 3.12) als Basis.
# Besteht aus einem minimalistischen Debian-System + Python.

WORKDIR /Webserver
# Setzt das Arbeitsverzeichnis im Container auf /Webserver.
# Alle folgenden Befehle (Copy, Run, etc) werden in diesem Verzeichnis ausgeführt.

COPY requirements.txt .
# Kopiert die Datei requirements.txt aus dem aktuellen Projektverzeichnis in den Containerpfad /Webserver/.
 
RUN pip install --no-cache-dir -r requirements.txt
# Installiert alle Python Abhänigkeiten, die in requirements.txt aufgelistet sind.
# --no-cache-dir spart Speicherplatz in dem es verhindert, dass pip zwischengespeicherte Dateien behält.
# -r sagt pip das es eine Datei mit Abhängigkeiten einlesen soll. Also eine Liste von Pakten, die installiert werden müssen.

COPY . .
# Kopiert den gesamten Inhalt des aktuellen Ordner in das Arbeitsverzeichnis im Container.

EXPOSE 5000
# Gibt Port 5000 im Container für Netzwerkzugriffe frei.
# Dies ist nur eine Info für Docker, den Port muss manuell freigeben werden.

CMD ["python", "app.py"]
# Startet das Python Programm app.py beim Container Start.
# In meinem Fall der Webserver (Flask App).
