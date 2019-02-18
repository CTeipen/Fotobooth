#!/bin/bash
echo "Start start.sh"

if [ $# -eq 8 ] && [ $1 == '-pc' ] && [ $3 == '-pu' ] && [ $5 == '-q' ] && [ $7 == '-t' ]
then
  echo "Anzahl der Parameter $#"
  echo "Pfad Cloud: $2"
  echo "Pfad USB: $4"
  echo "QR-Code: $6"
  echo "Zeit: $8"
  sleep 10
else
  echo 'Aufruf mit falschen Parametern'
  echo 'Beispiel: ./capturePic.sh -p PFAD_ZU_BILDERN -q URL_QR_CODE'
fi

echo "Ende start.sh"
