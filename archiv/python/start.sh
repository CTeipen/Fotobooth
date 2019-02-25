#!/bin/bash
echo "start.sh - Start Fotobox"

gphoto2 --capture-tethered --hook-script=test-hook.sh --filename=$1"photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite

if [ $# -eq 2 ]
then
  rsync -a $1 $2
fi

echo "start.sh - End Fotobox"
