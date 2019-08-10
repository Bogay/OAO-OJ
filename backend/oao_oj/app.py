import os
import pymongo
import json

from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS

from oao_oj.oj_mongo import update_problem, get_all_problems, get_problem, add_problem
from oao_oj.config import *

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
        return update_problem(pid, request.value)
    elif request.method == 'PUT':
        return add_problem(pid)


@app.route('/accounts', methods=['GET', 'POST', 'PUT'])
def account_entry():
    pass


@app.route('/submit', methods=['POST'])
def submit():
    pid = request.values.get('pid')

    if not pid:
        return jsonify({'err': 'no selected problem!'}), 400

    script = request.values.get('script', '').strip()
    in_data = request.values.get('input-data', '')
    out_data = request.values.get('output-data', '').strip()
    test = in_data or out_data

    response = {
        'scriptLen': len(script),
        'result': []
    }

    if any(c in script for c in ['\n', '\r', ';']):
        response['result'] = ['LLE']
        return jsonify(response), 200

    with open(f'{TMP_DIR}/a.py', 'w') as f:
        f.write(script)

    if test:
        response['taskCount'] = 1
        response['result'].append(judge(in_data, out_data))
    else:
        # read problem info
        try:
            info = json.loads(readAll(f'{PROB_DIR}/{pid}/info.json'))
        except:
            return jsonify({'err': 'judge error!'}), 500

        response['taskCount'] = len(info['testdatas'])
        for task, time_l, mem_l in info['testdatas']:
            in_data_path = f'{PROB_DIR}/{pid}/{TEST_DIR}/{task}.in'
            out_data_path = f'{PROB_DIR}/{pid}/{TEST_DIR}/{task}.out'
            response['result'].append(judge(in_data_path, out_data_path))

    return jsonify(response), 200

    
def judge(in_data_path, out_data_path):
    os.system(f'python3 {TMP_DIR}/a.py < {in_data_path} > {TMP_DIR}/a.out')

    user_out = readAll(f'{TMP_DIR}/a.out').rstrip()
    except_out = readAll(out_data_path).rstrip()

    if user_out == except_out:
        return 'AC'
    else:
        return 'WA'
