# Testen, welche Verbindungen (Apache Server) verfügbar sind
# duckduckgo.com down?, Localhost=127.0.0.1 ok, 127.24.0.5 ok
# 0.0.0.0 ok, 172.24.0.0-subnet ok, 172.24.0.1-gateway ok
# Der Websocket läuft auf Port 3000 und IPs 5, 2

import time
import os

IPs = ["40.114.177.156", "localhost", '127.24.0.0', '127.24.0.1', '172.24.0.5', '0.0.0.0',
       '172.24.0.5:3000', '172.24.0.2', '172.24.0.2:3000', '172.24.0.2:80']

for e in IPs:
    # Ping Abfrage, um die Verfügbarkeit zu testen
    # -n weist dem Befehl an, eine binäre Ausgabe zurückzugeben
    # -c 1 weist dem Befehl an, nur eine Anfrage abzuschicken
    # ping sendet standardmäßig eine sequenzielle Abfrage bis zum Abbruch
    response = os.system("ping -n -c 1 " + e)

    # Standard Zeitintervall zwischen den PING Ausführungen
    time.sleep(1)

    if response == 0:
        print(e, 'is up: ' + str(response) + '\n', flush=True)
    else:
        print(e, 'is down: ' + str(response) + '\n', flush=True)
