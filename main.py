#!/usr/bin/python
#-*-coding=utf-8

from flask import Flask
from flask import render_template
from config import Config
from module import user

app = Flask(__name__)
app.register_blueprint(user.user)
app.config.from_object(Config)
# default url_prefix = /
#app.register_blueprint(user, url_prefix='/reg')

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from module.model import User

@login_manager.user_loader
def load_user(userid):
    print "load user:",userid
    return User("username")

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html',title='main page')

@app.route('/hello/<name>')
def hello_name(name=None): 
    name="\<h1\>Haaa..\<\/h1\><h2>Maaaa</h2>"   
    return render_template('main.html',name=name)

@app.route('/testjs')
def testjs(): 
    content="<h1> h1 content <h1>"
    return render_template('jstest.html',content=content)

if __name__ == '__main__':
    app.run()
