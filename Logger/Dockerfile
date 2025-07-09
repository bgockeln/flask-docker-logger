FROM python:3.12-slim
# Benutzt ein Python-Image(Version 3.12 als Basis.
# Besteht aus einem minimalistischem Debian-System + Python.

WORKDIR /Logger
# Setzt das Arbeitsverzeichnis im Container auf /Logger
# Alle folgenden Befehle (Copy, Run, etc) werden in diesem Verzeichnis ausgeführt

COPY requirements.txt .
# Kopiert die Datei requirements-txt aus dem aktuellen Projektverzeichnis in den Containerpfad /Logger/

RUN pip install --no-cache-dir -r requirements.txt
# Installiert alle Python Abhängigkeiten, die in requirements.txt aufgelistet sind.
# --no-cache-dir spart Speicherplatz in dem es verhindert, das pip zwischengespeicherte Dateien behält.
# -r sagt pip das es eine Datei mit Abhängigkeiten einlesen soll. Also eine Liste von Paketen, die installiert werden müssen.

COPY . .
# Kopiert den gesamten Inhalt des aktuellen Ordners in das Arbeitsverzeichnis im Container.

EXPOSE 5001
# Gibt Port 5001 im Container für Netzwerkzugriffe frei.
# Dies ist nur eine Info für Docker, der Port muss manuell freigegeben werden.

CMD ["python", "logger.py"]
# Startet das Python Programm logger.py beim Container Start.
# In meinem Fall den Logger (Flask App)
