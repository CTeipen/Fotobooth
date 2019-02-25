#!/bin/bash

self=`basename $0`
echo "$self: START"

# 1 Cloud - 2 USB
if [ $# -eq 2 ]
then
	export CLOUDDIR="$1"
	export USBDIR="$2"
else
	export CLOUDDIR="$1"
	export USBDIR=""
fi		

echo "$self: CLOUDDIR $CLOUDDIR"
echo "$self: USBDIR $USBDIR"

gphoto2 --capture-tethered --hook-script=/home/pi/git/Fotobooth/hook.sh --filename=$CLOUDDIR"youinthebox-%Y%m%d-%H%M%S.%C" --force-overwrite

echo "$self: STOP"

exit 0


