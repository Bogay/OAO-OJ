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


@probs_api.route('/<pid>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def problem_entry(pid):
    method = request.method

    # Get a problem's detail
    if method == 'GET':
        prob_detail = Problem(pid).detail
        if not prob_detail:
            return jsonify({'err': 'Problem not exists.'}), 404

        return jsonify(prob_detail)

    # Add a new problem
    elif method == 'POST':
        data = request.values
        prob = Problem.add(pid, data)
        if not prob:
            return jsonify({'err': 'Problem exists.'}), 400

        return jsonify({'msg': 'Ok.'})

    # Update a problem
    elif method == 'PUT':
        data = request.values

        return Problem(pid).update(data)

    # Delete a problem
    elif method == 'DELETE':
        count = Problem(pid).delete()
        if not count:
            return jsonify({'err': 'Problem not exists.'}), 404

        return jsonify({'msg': 'Ok.'})
