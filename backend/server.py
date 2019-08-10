import os
import pymongo
from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS

from oj_mongo import update_problem, get_all_problems, get_problem, add_problem

app = Flask(__name__)
CORS(app)

def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


@app.route('/problems', methods=['GET'])
@app.route('/problems/<pid>', methods=['GET', 'POST', 'PUT'])
def problem_entry(pid = None):
    if request.method == 'GET':
        if pid:
            return get_problem(pid)
        else:
            return get_all_problems()
    elif request.method == 'POST':
        update_problem(pid, request.value)
    elif request.method == 'PUT':
        add_problem(pid)
    else:
        # not allowed method
        return '', 405


@app.route('/accounts', methods=['GET', 'POST', 'PUT'])
def account_entry():
    pass


@app.route('/', methods=['POST'])
def submit():
    script = request.values['script'].strip()
    inData = request.values.get('input-data', readAll(f'{TEST_DIR}/test.in'))
    outData = request.values.get('output-data', readAll(f'{TEST_DIR}/test.out')).strip()

    if any(c in script for c in ['\n', '\r', ';']):
        return jsonify({'result': 'LLE'})

    with open(f'{TMP_DIR}/a.py', 'w') as f:
        f.write(script)
    with open(f'{TMP_DIR}/a.in', 'w') as f:
        f.write(inData)

    os.system(f'cd {TMP_DIR} && python3 a.py < a.in > a.out')

    return jsonify({'result': ['WA', 'AC'][readAll(f'{TMP_DIR}/a.out').rstrip() == outData]})
