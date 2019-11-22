# Fotobooth
## Bedienungsanleitung

## Raspbian OS - Backup der SD Card
### Backup

Der erste Part liest die SD Card (if => input file) aus. Diese an der Schnittstelle „disk2“ des Rechners angeschlossen. Das gepipte „pv -s 32G“ zeigt den Fortschritt während des Kopierens mit der Angabe, um wie viel GB es sich bei dem Vorgang handelt (hier 32GB). Der dritte Teil ist das Schreiben des if in die Zieldatei (of => Output File). Die Zieldatei heißt bspw. „Fotobox-2019-11-21.dmg“.

```sudo dd bs=4m if=/dev/disk2 | pv -s 32G | sudo dd of=~/Desktop/fotobox-`date +%Y-%m-%d`.dmg```

### Restore

Über das Programm [balenaEtcher](https://www.balena.io/etcher/)
