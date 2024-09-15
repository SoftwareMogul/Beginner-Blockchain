import os, random

from flask import Flask, jsonify
from backend.pubsub import PubSub

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub()

for i in range(3):
    blockchain.add_block(i)

@app.route('/')
def route_default():
    return 'Welcome to the Blockchain.'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

app.run(port=PORT)