#!/bin/bash
until sudo python3 ~/Desktop/C3PO/Bot.py; do
    echo "'Bot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
