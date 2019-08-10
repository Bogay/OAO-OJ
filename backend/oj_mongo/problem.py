
import pymongo
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from config import *
from flask import jsonify

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
oj_db = mongo_client['OAO-OJ']


def update_problem(pid, data):
    title = data.get('title')
    content = data.get('content')

    if not (pid and title and content):
        return jsonify({'msg': 'missing data!'}), 404


def get_all_problems():
    ps_col = oj_db[PROB_COL]
    ps = [*ps_col.find({}, {'_id': 0, 'pid': 1, 'title': 1})]
    ps = [[p['pid'], p['title'], 0, 0] for p in ps]

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
    except:
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
