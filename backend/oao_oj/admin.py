from flask import Blueprint, request, jsonify

from oao_oj.mongo import Problem, get_all_problems

admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/probs', methods=['GET'])
def problems_list():
    ps = get_all_problems()
    ps = [{
        'pid': p.get('pid', ''), 
        'title': p.get('title', ''), 
        'status': p.get('status', 0),
    } for p in ps]

    return jsonify(ps)


@admin_api.route('/probs/<pid>', methods=['POST', 'PUT', 'DELETE'])
def manage_problem(pid):
    method = request.method
    data = request.json

    # Add a new problem
    if method == 'POST':
        try:
            Problem.add(pid, data)
        except Exception as e:
            return e.response

        return jsonify({'msg': f'Problem (pid={pid}) is added.'})

    # Update a problem
    elif method == 'PUT':

        try:
            Problem(pid).update(data)
        except Exception as e:
            return e.response

        return jsonify({'msg': f'Problem (pid={pid}) is updated.'})

    # Delete a problem
    elif method == 'DELETE':
        try:
            Problem(pid).delete()
        except Exception as e:
            return e.response

        return jsonify({'msg': f'Problem (pid={pid}) is deleted.'})
