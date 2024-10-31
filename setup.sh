#!/bin/bash

# تثبيت المتطلبات
echo "Installing Python dependencies..."
pip install -r requirements.txt

# تشغيل التطبيق
echo "Running the main script..."
python app.py
