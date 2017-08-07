from . import main
from flask import render_template, jsonify
from flask import current_app as app
import json


@main.route('/')
def index():
    with main.open_resource(app.config['JSON_PATH']) as infile:
        data = json.load(infile)
        price_str = "%.2f" % data["RAW"]["NEO"]["USD"]["PRICE"]
        low_str = "%.2f" % data["RAW"]["NEO"]["USD"]["LOW24HOUR"]
        high_str = "%.2f" % data["RAW"]["NEO"]["USD"]["HIGH24HOUR"]
        change = data["RAW"]["NEO"]["USD"]["CHANGE24HOUR"]
        change_str = "%.2f" % abs(change)
    return render_template('index.html', price=price_str, low=low_str, high=high_str, change=change_str, decrease=change<0)


@main.route('/price')
def price():
    with main.open_resource(app.config['JSON_PATH']) as infile:
        data = json.load(infile)
        price_str = "%.2f" % data["RAW"]["NEO"]["USD"]["PRICE"]
        low_str = "%.2f" % data["RAW"]["NEO"]["USD"]["LOW24HOUR"]
        high_str = "%.2f" % data["RAW"]["NEO"]["USD"]["HIGH24HOUR"]
        change = data["RAW"]["NEO"]["USD"]["CHANGE24HOUR"]
        change_str = "%.2f" % abs(change)
    return jsonify({'price': price_str, 'low': low_str, 'high': high_str, 'change': change_str, 'decrease': change<0})
