import os
import json

from flask import Blueprint, request, jsonify

from oao_oj.config import PROB_DIR, TEST_DIR, TMP_DIR

judge_api = Blueprint('judge_api', __name__)


def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


@judge_api.route('/submit', methods=['POST'])
def submit():
    pid = request.values.get('pid')

    if not pid:
        return jsonify({'err': 'no selected problem!'}), 400

    script = request.values.get('script', '').strip()
    in_data = request.values.get('input-data', '')
    out_data = request.values.get('output-data', '').strip()

    response = {
        'scriptLen': len(script),
        'results': []
    }

    if any(c in script for c in ['\n', '\r', ';']):
        response['results'] = ['LLE']
        return jsonify(response), 200

    with open(f'{TMP_DIR}/a.py', 'w') as f:
        f.write(script)

    if in_data or out_data:
        in_data_path = f'{TMP_DIR}/user.in'
        out_data_path = f'{TMP_DIR}/user.out'

        with open(in_data_path, 'w') as f:
            f.write(in_data)
        with open(out_data_path, 'w') as f:
            f.write(out_data)

        response['taskCount'] = 1
        response['results'].append(judge(in_data_path, out_data_path))

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
            response['results'].append(judge(in_data_path, out_data_path))

    return jsonify(response), 200

    
def judge(in_data_path, out_data_path):
    os.system(f'python3 {TMP_DIR}/a.py < {in_data_path} > {TMP_DIR}/a.out')

    actual_out = readAll(f'{TMP_DIR}/a.out').rstrip()
    except_out = readAll(out_data_path).rstrip()

    if actual_out == except_out:
        return 'AC'
    else:
        return 'WA'
