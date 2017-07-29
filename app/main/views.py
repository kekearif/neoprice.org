from . import main
from flask import render_template, jsonify
import json


@main.route('/')
def index():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
        price_str = "%.2f" % data["RAW"]["ANS"]["USD"]["PRICE"]
        low_str = "%.2f" % data["RAW"]["ANS"]["USD"]["LOW24HOUR"]
        high_str = "%.2f" % data["RAW"]["ANS"]["USD"]["HIGH24HOUR"]
        change = data["RAW"]["ANS"]["USD"]["CHANGE24HOUR"]
        change_str = "%.2f" % abs(change)
    return render_template('index.html', price=price_str, low=low_str, high=high_str, change=change_str, decrease=change<0)


@main.route('/price')
def price():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
        price_str = "%.2f" % data["RAW"]["ANS"]["USD"]["PRICE"]
        low_str = "%.2f" % data["RAW"]["ANS"]["USD"]["LOW24HOUR"]
        high_str = "%.2f" % data["RAW"]["ANS"]["USD"]["HIGH24HOUR"]
        change = data["RAW"]["ANS"]["USD"]["CHANGE24HOUR"]
        change_str = "%.2f" % abs(change)
    return jsonify({'price': price_str, 'low': low_str, 'high': high_str, 'change': change_str, 'decrease': change<0})
