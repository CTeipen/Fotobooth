#!/bin/bash

self=`basename $0`

echo $1

case "$ACTION" in
    init)
	echo "$self: INIT"	
	;;

    start)
		echo "$self: START"
		echo "ARGUMENT: $ARGUMENT"
		echo "Cloud Directory: $CLOUDDIR"
		echo "USB Directory : $USBDIR"
	;;

    download)
		echo "$self: DOWNLOAD to $ARGUMENT"
		
		# Dateigröße reduzieren (dauert auf dem Pi u lange...)
		# convert -quality 40 "$ARGUMENT" "$CLOUDDIR$ARGUMENT" && echo 'File Size reduced'
		cp "$ARGUMENT" "$CLOUDDIR$ARGUMENT"

		# nach abgeschlossenem Download der Bilder, kopieren auf USB Stick
		if [ ! -z "$USBDIR" ]
		then
			cp "$ARGUMENT" "$USBDIR$ARGUMENT"
		fi

		# Dateigröße reduzieren
		# convert -quality 50 "$ARGUMENT" "$ARGUMENT-1" && echo 'File Size reduced'
		# composite -dissolve 50% -gravity SouthEast watermark.png "$ARGUMENT" "$USBDIR/watermarked-$ARGUMENT"
		
		/home/pi/git/Fotobooth/slideshow.sh "$ARGUMENT" &

	;;

    stop)
	echo "$self: STOP"
	;;

    *)
	echo "$self: Unknown action: $ACTION"
	;;
esac

exit 0
