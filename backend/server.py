from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from oao_oj.admin import admin_api
from oao_oj.judge import judge_api
from oao_oj.probs import probs_api
from oao_oj.users import users_api, login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vcde4567ujbvfgtyu78iokjbg7'

app.register_blueprint(admin_api, url_prefix='/admin')
app.register_blueprint(judge_api, url_prefix='/judge')
app.register_blueprint(probs_api, url_prefix='/probs')
app.register_blueprint(users_api, url_prefix='/users')

CORS(app)

login_manager.init_app(app)