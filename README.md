# Fotobooth
## Vorbereitung

Um das Projekt nutzen zu können, kann es entweder per Konsole oder aus dem Browser geladen werden.

### Browser

Auf der Seite ![https://github.com/CTeipen/Fotobooth]{Fotobooth - Github} befinden sich oben 
rechts ein Button "Clone or Download". Betätigt man diesen kann das Projekt als Zip-Datei heruntergeladen werden. 
Nach dem Entpacken der Zip-Datei, geht es mit dem Kapitel "Benutzung" weiter.

### Terminal

Auf der Konsole sind folgende Befehle auszuführen:

sudo apt-get intall git

mkdir ~/git

cd ~/git

git clone https://github.com/CTeipen/Fotobooth.git

cd Fotobooth

## Benutzung

Über die Konsole in das Verzeichnis des Fotobooth-Projektes navigieren ("cd PFAD") und folgenden Befehl ausführen:

./start.sh -p PFAD_IN_DEM_DIE_BILDER_GESPEICHERT_WERDEN_SOLLEN -q URL_DIE_ALS_QR_CODE_GENERIERT_WIRD

Die Parameter -p und -q können so gesetzt werden, dass die Bilder in einem Ordner (-p) gespeichert werden, 
der mittels eines Cloud Clients direkt synchronisiert wird. Wenn man nun diesen Ordner freigibt und den Link als Parameter 
-q übergibt, kann der erzeugte QR-Code in der Nähe der Fotobox angebracht werden. Benutzer der Fotobox können dann nach dem 
Fotoshooting den QR-Code mittels Smartphone scannen und direkt auf alle gemachten Bilder zugreifen.

Hinweis: Der QR-Code wird im Ordner gespeichert, der auch für die Fotos (-p) angegeben wird.
