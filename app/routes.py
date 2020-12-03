from app import app
from flask import json, render_template


@app.route('/')
@app.route('/knitting-calculator')
def knitting_calulator():
    return render_template('knitting_calculator/knitting_calculator.html')


@app.route('/knitting-calculator/calculate')
def knitting_calculator_json():
    return json.jsonify({'a': 1})

