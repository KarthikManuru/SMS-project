#!/usr/bin/env bash
apt-get update && apt-get install -y build-essential python3-dev cargo rustc
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
