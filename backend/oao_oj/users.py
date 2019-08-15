from flask import Blueprint

users_api = Blueprint('users_api', __name__)


@users_api.route('/', methods=['GET', 'POST', 'PUT'])
def user_entry():
    return 'users'
