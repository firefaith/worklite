#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, Blueprint
from flask_login import LoginManager, login_required
from flask import request

app1 = Flask(__name__)

# 以下这段是新增加的============
app1.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app1)

@login_manager.user_loader
def load_user(user_id):
    return None
# 以上这段是新增加的============

auth = Blueprint('auth', __name__)

@app1.route('/')
def hello():
    return "Hello"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    print request.headers
    return "login page"

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    return "logout page"

# test method
@app1.route('/test')
@login_required
def test():
    return "yes , you are allowed"

app1.register_blueprint(auth)
app1.run(debug=True,port=5001)