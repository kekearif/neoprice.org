from . import main
from flask import render_template, jsonify
import json


@main.route('/')
def index():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
    return render_template('index.html', price=data["USD"])


@main.route('/price')
def price():
    with main.open_resource("../static/prices.json") as infile:
        data = json.load(infile)
    return jsonify({'value': data["USD"]})
