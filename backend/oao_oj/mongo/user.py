import random

from oao_oj.config import OJ_DB, USER_COL

USER_COLL = OJ_DB[USER_COL]

class User:
    def __init__(self, uid):
        self.uid = uid

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uid


def get_user_by_uid(uid):
    user = USER_COLL.find_one({'uid': uid})
    if not user:
        return None
    else:
        return User(user['uid'])


def get_uid_by_username(username):
    user = USER_COLL.find_one({'username': username})
    if not user:
        return None
    else:
        return user['uid']

def generate_uid():
    return str(random.random())[2:]

def new_user(username, password):
    # WARN: no check for duplicate username
    uid = generate_uid()
    while USER_COLL.find_one({'uid': uid}):
        uid = generate_uid()

    USER_COLL.insert_one({
        'uid': uid,
        'username': username,
        'password': password
    })


def validate_user(uid, password):
    user = USER_COLL.find_one({'uid': uid})
    print(user)
    print(password)
    # TODO: more info
    if not user:
        return False
    return password == user['password']