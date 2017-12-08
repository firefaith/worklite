from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

testsql = Flask(__name__)
db = SQLAlchemy(testsql)
testsql.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
"""
>>> from testSql import db
/Library/Python/2.7/site-packages/flask_sqlalchemy/__init__.py:774: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
/Library/Python/2.7/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> from testSql import User
>>> testsql.db.createall()
>>> admin = User('admin', 'admin@example.com')
>>> guest = User('guest', 'guest@example.com')
>>> admin
<User 'admin'>
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()
>>> users = User.query.all()
>>> users
[<User u'admin'>, <User u'guest'>]
"""