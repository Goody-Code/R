#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting the syslog daemon and web server..."
python3 app.py
