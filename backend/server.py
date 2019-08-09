import os
import pymongo
from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS

# constants for path
TMP_DIR = 'tmp'
TEST_DIR = 'testdata'
PROB_DIR = 'prob'

# constants for db
PROB_COL = 'problems'

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
oj_db = mongo_client['OAO-OJ']

app = Flask(__name__)
CORS(app)

def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


def update_problem(pid, data):
    title = data.get('title')
    content = data.get('content')

    if not (pid and title and content):
        return jsonify({'msg': 'missing data!'}), 404


def get_all_problems():
    ps_col = oj_db[PROB_COL]
    ps = [*ps_col.find({}, {'_id': 0, 'pid': 1, 'title': 1})]

    return jsonify(ps), 200


def get_problem(pid):
    ps_col = oj_db[PROB_COL]
    prob = ps_col.find_one({'pid': pid})

    if not prob:
        return jsonify({'msg': f'pid {pid} not found!'}), 404

    # read problem content
    try:
        with open(f'{PROB_DIR}/{pid}/prob.md') as f:
            desc = f.read()
    except e:
        return jsonify({'msg': f'error when reading problem\'s content!'}), 404

    prob = {
        'pid': prob['pid'],
        'title': prob['title'],
        'desc': desc
    }

    return jsonify(prob), 200

def add_problem(pid):
    ps_col = mongo_client[PROB_COL]

    if ps_col.find_one({'pid': pid}):
        return jsonify({'msg': f'the problem ID {pid} exists'}), 400

    # TODO: check for problem data

    ppath = f'{PROB_DIR}/{pid}'

    try:
        os.makedirs(ppath)
    except:
        return jsonify({'msg': 'error when writing problem content!'}), 400

    # write problem description
    with open(f'{ppath}/prob.md', 'w') as f:
        f.write(request.value.get('desc'))

    # insert to db
    ps_col.insert_one({
        'pid': pid,
        'title': request.vlaue.get('title')
    })

    # TODO: write testdata

    return jsonify({'msg': f'problem {pid} has been created'}), 201

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
