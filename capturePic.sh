#!/bin/bash

# Setzt den Auslöse-Modus der Kamera auf die Fernbedienung
# gphoto2 --set-config-index /main/capturesettings/capturemode=4

# Darstellung eines schwarzen Bildes im Vollbildmodus (vermutlich möchte niemand das Terminal sehen)
# eog -f -w util/blackscreen.png &

# Generierung eines QRCodes
qrencode -o util/qrcode.png -s 10 'URL: http://cloud.cteipen.de/index.php/s/zVAFlt5kTLbblLK'

# Aktivierung des Tethering-Modus der Kamera und Warten auf Bilder
gphoto2 --capture-tethered --hook-script=test-hook.sh --filename="booth/photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite
