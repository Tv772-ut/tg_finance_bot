from flask import Flask, jsonify, request
from models import Session, Record, UserWallet

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'status': 'ok', 'message': 'Welcome to WebApp 🧠'})

@app.route('/records')
def get_records():
    session = Session()
    records = session.query(Record).all()
    return jsonify([{
        'id': r.id,
        'amount': r.amount,
        'note': r.note,
        'category': r.category,
        'created_at': r.created_at.isoformat()
    } for r in records])

@app.route('/wallets')
def get_wallets():
    session = Session()
    wallets = session.query(UserWallet).all()
    return jsonify([{
        'user_id': w.user_id,
        'address': w.address,
        'remark': w.remark,
        'phone_number': w.phone_number
    } for w in wallets])

if __name__ == '__main__':
    app.run()
