#!/bin/bash
cd "$(dirname "$0")"
export FLASK_APP=web/app.py
export FLASK_ENV=production
source .env
python3 web/app.py
