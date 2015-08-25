from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask.ext.login import login_user , logout_user , current_user , login_required
from werkzeug import check_password_hash, generate_password_hash
from app.user.models import User
from app import db, login_manager

gUser = Blueprint('user', __name__, url_prefix='/user')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@gUser.route('/signup' , methods=['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('user/login.html')
	user = User(request.form['username'] , request.form['password'],request.form['email'])
	db.session.add(user)
	db.session.commit()
	flash('User successfully registered')
	return redirect(url_for('welcome'))

@gUser.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('user/login.html')
	email=request.form['Email']
	password=request.form['Password']
	registered_user = User.query.filter(User.email==email).first()
	if registered_user is None:
		flash('Username or Password is invalid' , 'error')
		return redirect(url_for('welcome'))
	login_user(registered_user)
	ulog= current_user
	flash('Logged in successfully')
	return  redirect(url_for('home'))

@gUser.route('/logout', methods=['GET','POST'])
@login_required
def logout():
	logout_user()


