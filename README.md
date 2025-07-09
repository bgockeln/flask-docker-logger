# Flask Logging Projekt

Um praktische Erfahrungen im Umgang mit Linux-Servern zu sammeln, habe ich ein kleines Website-Logging-System erstellt.
Ziel war es, auf einem Linux-Server zwei Docker-Container zu betreiben:

* Der erste Container enthält eine Website, auf der Besucher ihre IP-Adresse abfragen können.
* Der zweite Container übernimmt das Logging. Jede Anfrage wird entgegengenommen und mit Zeitstempel in einer .txt-Datei gespeichert.

Die Entwicklung erfolgte auf einem virtuellen Ubuntu-Server in VirtualBox. Später wurde das Projekt zusätzlich auf einem 
Debian-Server getestet. Die Verbindung zu den Servern erfolgte ausschließlich per SSH über ein WSL-Debian-Terminal unter Windows. 
Der gesamte Prozess lief bewusst nur im Terminal ab, um möglichst realitätsnahe Serveradministration zu üben.

Es handelt sich um mein erstes Projekt dieser Art. Ich beanspruche daher nicht, jede einzelne Zeile Code vollständig zu verstehen. 
Ein grundlegendes Verständnis in den Bereichen Linux, Docker und Python ist jedoch vorhanden und wurde durch das Projekt 
weiter vertieft.

** Zur Klarstellung: **
Die HTML- und CSS-Dateien wurden mithilfe von ChatGPT generiert. Da mein Fokus auf Linux und Docker lag, habe ich diesen Teil bewusst abgekürzt. Auch hier verfüge ich jedoch über ein grundlegendes Verständnis. 
Der übrige Projektcode wurde teilweise mit Unterstützung von ChatGPT erstellt, jedoch zu keiner Zeit per „Copy and Paste“ übernommen.

---

## Verwendete Technologien
* Python 3.12
* Flask
* Docker
* HTTP + CSS

---

## Quellen
* [W3Schools](https://www.w3schools.com/)
* [ChatGPT](https://chatgpt.com/)
* [geeksforgeeks.org](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
* [Offizielle Python Dokumentation](https://docs.python.org/3/)
