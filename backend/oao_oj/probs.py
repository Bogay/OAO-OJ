from flask import Blueprint, request, jsonify

from oao_oj.mongo import Problem, get_all_problems

probs_api = Blueprint('probs_api', __name__)


@probs_api.route('/', methods=['GET'])
def problems_list():
    probs = get_all_problems()
    probs = [{
        'pid': p['pid'], 
        'title': p['title'], 
        'status': 0,
        'submissionsAcRate': 0,
        'usersAcRate': 0
    } for p in probs]

    return jsonify(probs)


@probs_api.route('/<pid>', methods=['GET'])
def problem_detail(pid):
    prob = Problem(pid)

    try:
        prob_dt = prob.detail()
    except Exception as e:
        return e.response

    prob_detail = {
        'pid': prob_dt['pid'],
        'title': prob_dt['title'],
        'desc': prob.desc
    }

    return jsonify(prob_detail)
