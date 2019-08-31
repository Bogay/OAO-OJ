import re

from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user

from oao_oj.mongo.user import User, get_uid_by_username, validate_user, get_user_by_uid, new_user

users_api = Blueprint('users_api', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(uid):
    return get_user_by_uid(uid)


@users_api.route('/login', methods=['POST'])
def user_login():
    username = request.values.get('username')
    password = request.values.get('password')
    if not username or not password:
        return jsonify({'err': 'please fill in the username and password field'}), 400

    uid = get_uid_by_username(username)
    user = get_user_by_uid(uid)
    if not uid or not user:
        return jsonify({'err': 'user not found'}), 401

    password = hash('OAO-OJ' + username + password)
    if validate_user(uid, password):
        login_user(user)
        return jsonify({'msg': 'login successed'}), 200
    else:
        return jsonify({'msg': 'wrong username or password'}), 401
    

@users_api.route('/sign-up', methods=['POST'])
def user_sign_up():
    username = request.values.get('username')
    password = request.values.get('password')
    if not username or not password:
        return jsonify({'err': 'please fill in the username and password field'}), 400

    uid = get_uid_by_username(username)
    if uid:
        return jsonify({'msg': 'the username has been registered'}), 401

    password = hash('OAO-OJ' + username + password)
    new_user(username, password)

    return jsonify({'msg': 'sign up successful'}), 200


@users_api.route('/info', methods=['POST'])
def user_info():
    pass
