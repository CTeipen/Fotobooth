#!/bin/bash
cd /home/pi/git/Fotobooth/
git pull
chmod 755 main.py
chmod 755 *.sh
shutdown -r -t 0
