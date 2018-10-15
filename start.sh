#!/bin/bash

if [ $# -eq 4 ] && [ $1 == '-p' ] && [ $3 == '-q' ]
then

    # Setzt den Auslöse-Modus der Kamera auf die Fernbedienung
    # gphoto2 --set-config-index /main/capturesettings/capturemode=4

    # Darstellung eines schwarzen Bildes im Vollbildmodus (vermutlich möchte niemand das Terminal sehen)
    # eog -f -w util/blackscreen.png &
     
    # Generierung eines QRCodes
    qrencode -o $2"qrcode.png" -s 10 $4

    # Aktivierung des Tethering-Modus der Kamera und Warten auf Bilder
    gphoto2 --capture-tethered --hook-script=test-hook.sh --filename=$2"photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite

else

    echo 'Aufruf mit falschen Parametern'
    echo 'Beispiel: ./capturePic.sh -p PFAD_ZU_BILDERN -q URL_QR_CODE'

fi
