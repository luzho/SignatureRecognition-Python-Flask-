from flask import Flask, request, render_template, flash, g, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.login import login_user , logout_user , current_user , login_required

app = Flask (__name__, template_folder = 'templates',static_folder = 'statics')
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.user.controllers import gUser as userModule


@app.route('/')
def welcome():
	return render_template('user/login.html')

@app.before_request
def before_request():
    g.user = current_user	

@app.route('/home',methods=['GET','POST'])
@login_required
def home():
	if request.method == 'GET':
		return render_template('user/home.html')
	

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('welcome'))




app.register_blueprint(userModule)