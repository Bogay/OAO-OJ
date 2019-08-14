from flask import Blueprint, request, jsonify
from oao_oj.mongo import get_all_problems

admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/problems', methods=['GET'])
def problem_entry():
    ps = get_all_problems()
    ps = [{
        'Id': p['pid'], 
        'Name': p['title'], 
        'Status': 'Online',
    } for p in ps]

    return jsonify(ps)
