#!/bin/bash

killall feh # schließen der aktuell laufenden Slideshow

# Anzeige des aktuell geknipsten Bildes für 5 Sekunden, danach Start der Slideshow
# Option -F steht für "Vollbild", --cycle-once sorgt dafür, dass das Programm
# nach der eingestellten Anzeigedauer von -D 3 (3 Sekunden) nicht neu gestartet wird.
# Ist die Ausführung des ersten feh-Aufrufs beendet, folgt der zweite Aufruf mit allen
# jpg-Bilder im Unterordner slideshow. -R 2 bedeutet, dass alle 2 Sekunden die
# Dateiliste neu geladen wird, so dass auch neu hinzugefügte Bilder angezeigt
# werden.
FILENAME=$1
SLIDES=${FILENAME::-31}'*.jpg'
feh -F --cycle-once -D 8 $1 --hide-pointer && feh -F -R 2 -D 3 $SLIDES --randomize --hide-pointer
