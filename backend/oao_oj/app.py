import os
import pymongo
import json

from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS

from oao_oj.mongo import Problem, get_all_problems
from oao_oj.config import *
from oao_oj.admin import admin_page

app = Flask(__name__)
app.register_blueprint(admin_page, url_prefix='/admin')
CORS(app)

def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


@app.route('/problems', methods=['GET'])
@app.route('/problem/<pid>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def problem_entry(pid=None):
    if not pid:
        return get_all_problems()

    method = request.method

    if method == 'GET':
        json = Problem(pid).json
        if not json:
            return jsonify({'err': 'Problem not exists.'}), 404

        return json

    elif method == 'POST':
        data = request.values
        prob = Problem.add(pid, data)
        if not prob:
            return jsonify({'err': 'Problem exists.'}), 400

        return jsonify({'msg': 'Ok.'})

    elif method == 'PUT':
        data = request.values

        return Problem(pid).update(data)

    elif method == 'DELETE':
        count = Problem(pid).delete()
        if not count:
            return jsonify({'err': 'Problem not exists.'}), 404

        return jsonify({'msg': 'Ok.'})


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
