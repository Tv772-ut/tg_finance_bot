#!/bin/bash

echo "🌐 正在启动 Web 控制面板..."
source .env
gunicorn -w 2 -b 0.0.0.0:8000 web.app:app
