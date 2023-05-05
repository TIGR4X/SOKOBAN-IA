#!/bin/bash
for f in "$@"
do
    python3 main.py "$f"
done
read -p "Presiona cualquier tecla para salir..." -n 1 -s