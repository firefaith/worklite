from flask import Flask
from flask import Blueprint, render_template, abort, flash, redirect, request, url_for
from jinja2 import TemplateNotFound
from flask_login import login_user
from model import User

user = Blueprint('user', __name__,template_folder='templates')

@user.route('/reg',methods=['POST','GET'])
def reg():
	if request.method=='GET':
		return render_template('reg.html')
	else:
		return "{},{}".format(request.form['user'],request.form['password'])

from .form import LoginForm

@user.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# Login and validate the user.
	  	# user should be an instance of your `User` class
		u = User(form.username)
		print u.username,'login'
		login_user(u)
		flash('Logged in successfully.')
		next = request.args.get('next')
		return redirect(next or url_for('hello_world'))
	return render_template('login.html',
						   title = 'Sign In',
						   form = form)
