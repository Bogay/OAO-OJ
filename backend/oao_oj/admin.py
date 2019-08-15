from flask import Blueprint, request, jsonify
from oao_oj.mongo import get_all_problems

admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/probs', methods=['GET'])
def problems_list():
    ps = get_all_problems()
    ps = [{
        'pid': p['pid'], 
        'title': p['title'], 
        'status': 1,
    } for p in ps]

    return jsonify(ps)
