from . import main
from flask import jsonify
from flask import render_template
import requests
import json


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/price')
def price():
    resp = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ANS&tsyms=BTC,USD")
    data = json.loads(resp.text)
    return jsonify({'value': data["USD"]})
