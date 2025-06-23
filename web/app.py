# web/app.py
from flask import Flask, jsonify
from models.init import init_db
import os

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return jsonify({'message': '未来科技记账机器人 Web 控制端运行中'})

if __name__ == '__main__':
    port = int(os.getenv("WEB_PORT", 8080))
    app.run(host='0.0.0.0', port=port)
