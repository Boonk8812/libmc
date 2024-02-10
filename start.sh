#!/bin/bash
cd "$(dirname "$0")"

# Optional: Clear screen before showing output
clear

echo "Starting libmc..."
PATH_TO_PYTHON="/usr/bin/python3" # Or wherever your preferred Python interpreter resides
$PATH_TO_PYTHON libmc.py
