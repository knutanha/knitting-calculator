from app import app
from app.knitting_calculator import calculator as knit_calc
from flask import json, render_template, request


@app.route('/')
def domain_index():
    return 'This is the index page.'


@app.route('/knitting-calculator')
def knitting_calulator():
    return render_template('knitting_calculator/knitting_calculator.html')


@app.route('/knitting-calculator/calculate', methods=['GET', 'POST'])
def knitting_calculator_json():
    init = request.args.get('init')
    target = request.args.get('target')
    try:
        init = int(init)
        target = int(target)
    except ValueError:
        return 'Error: 418'
    data = {'steps': [{'step': step, 'target': target, 'init': init} for step in range(target, init)],
            'result': knit_calc.calc_knit(init, target)}
    # data = {'steps': [{'step': step, 'target': target, 'init': init} for step in range(target, init)]}
    return render_template('knitting_calculator/knitting_result_alt.html', data=data)
