from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    orderer_receive = request.form['orderer_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phoneNumber_receive = request.form['phoneNumber_give']

    doc = {
        'orderer': orderer_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phoneNumber': phoneNumber_receive
    }

    db.orders.insert_one(doc)
    return jsonify({'msg': '정상적으로 주문되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)







