#!/bin/bash

INPUTFILE=$1 # Filename wird als Parameter übergeben

# Definition des Output-Filenamen. Hierfür wird vom Namen des Inputfiles "NEF" durch "jpg" getauscht, sowie "booth" durch "finish"
outputfile=`echo $INPUTFILE | sed s/NEF/jpg/g | sed s/booth/finish/g`

echo "start darktable, convert to $outputfile" # Ausgabe in Terminal, nur zu debug-Zwecken

# Das Lightroom-Pendant "darktable" wird mit dem Rawfile und der Preset-Datei "vorlage.xmp" aufgerufen und das Ergebnis als jpg gespeichert. Wenn dies beendet wurde, wird der generierte QR-Code als Overlay einer Bildkopie hinzugefügt. Das Urpsrungsfile bleibt hierbei unverändert
darktable-cli $INPUTFILE vorlage.xmp $outputfile && convert $outputfile util/qrcode.png -geometry +5500+3500 -composite booth/$outputfile && mv $outputfile finish/

