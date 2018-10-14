#!/bin/bash

self=`basename $0`

case "$ACTION" in
    init)
	echo "$self: INIT"
	
	;;
    start)
	echo "$self: START"
	;;
    download)
	echo "$self: DOWNLOAD to $ARGUMENT"
		# nach abgeschlossenem Download der Bilder

		TYPE=`file --mime-type -b "$ARGUMENT"` # Typ des Bildes herausfinden
	
        if [ "$TYPE" = 'image/tiff' ]; then # Falls es sich um ein War-Foto handelt ...
					echo "Hier wäre konvertiert worden" &
					#./convertPicture.sh $ARGUMENT &
        else # fuer das jpg-Bild
					#./convertPicture.sh $ARGUMENT &
					./startSlideshow.sh "$ARGUMENT" &

        fi


	;;
    stop)
	echo "$self: STOP"
	;;
    *)
	echo "$self: Unknown action: $ACTION"
	;;
esac

exit 0
