#!/bin/bash


### Uhrzeit
echo "Ist die Uhrzeit/Datum korrekt? [j/n]"
read timebool

if [ $timebool == 'n' ]
then
	echo "Wie ist die aktuelle Uhrzeit? (02 FEB 2019 22:18:00)"
	read time

	sudo date -s "$time"
fi


### Speicherort
echo "Wo sollen die Bilder gespeichert werden? (/home/fotobox/Bilder/)"
read pfad

if [ $pfad == '' ]
then
	pfad="/home/fotobox/Bilder/"
fi


### QR-Code
echo "Soll ein QR-Code angefertigt werden? [j/n]"
read qrbool

if [ $qrbool == 'j' ]
then
	echo "Wo soll der QR-Code hinführen?"
	read qrcontent

	qrencode -o $pfad"qrcode.png" -s 10 $qrcontent
fi

gphoto2 --capture-tethered --hook-script=test-hook.sh --filename=$pfad"photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite



#if [ $# -eq 4 ] && [ $1 == '-p' ] && [ $3 == '-q' ]
#then

    # Setzt den Auslöse-Modus der Kamera auf die Fernbedienung
    # gphoto2 --set-config-index /main/capturesettings/capturemode=4

    # Darstellung eines schwarzen Bildes im Vollbildmodus (vermutlich möchte niemand das Terminal sehen)
    # eog -f -w util/blackscreen.png &
     
    # Generierung eines QRCodes
    #qrencode -o $2"qrcode.png" -s 10 $4

    # Aktivierung des Tethering-Modus der Kamera und Warten auf Bilder
    #gphoto2 --capture-tethered --hook-script=test-hook.sh --filename=$2"photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite

#else

    #echo 'Aufruf mit falschen Parametern'
    #echo 'Beispiel: ./capturePic.sh -p PFAD_ZU_BILDERN -q URL_QR_CODE'

#fi
