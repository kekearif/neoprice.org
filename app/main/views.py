from . import main
from flask import render_template, jsonify
import json


@main.route('/')
def index():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
        usd_str = "%.2f" % data["USD"]
    return render_template('index.html', price=usd_str)


@main.route('/price')
def price():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
        usd_str = "%.2f" % data["USD"]
    return jsonify({'value': usd_str})
