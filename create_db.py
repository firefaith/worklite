#!/usr/bin/python
# create database
# sudo pip install sqlalchemy-migrate
# output : app.db and db_repository
# SQLALCHEMY_DATABASE_URI 是 Flask-SQLAlchemy 扩展需要的。这是我们数据库文件的路径。
# SQLALCHEMY_MIGRATE_REPO 是文件夹，我们将会把 SQLAlchemy-migrate 数据文件存储在这里。

from migrate.versioning import api
from config import Config
from main import db
import os.path
db.create_all()
if not os.path.exists(Config.SQLALCHEMY_MIGRATE_REPO):
    api.create(Config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO, api.version(Config.SQLALCHEMY_MIGRATE_REPO))