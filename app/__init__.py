import os
import Main
import cv2
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask, request, render_template, flash, g, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.login import login_user , logout_user , current_user , login_required
from werkzeug import secure_filename

app = Flask (__name__, template_folder = 'templates',static_folder = 'statics')

app.config['UPLOAD_FOLDER'] = 'app/statics/temp/'
app.config['ALLOWED_EXTENSIONS'] = set(['pdf', 'png', 'jpg', 'jpeg'])

app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.user.controllers import gUser as userModule

#--------------------------------------------------------------------------------------------------------
def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

#--------------------------------------------------------------------------------------------------------

@app.route('/')
def welcome():
	if current_user.is_authenticated():
		return redirect(url_for('home'))
	else:
		return render_template('user/login.html')

@app.before_request
def before_request():
    g.user = current_user	

@app.route('/home',methods=['GET','POST'])
@login_required
def home():

	if request.method == 'GET':
		control=None
		return render_template('user/home.html',**locals())
		

	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file1,exten=filename.split(".")
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			if exten == "pdf":
				Main.convert("app/statics/temp/"+filename,"/home/carlos/Projects/line-recognition/app/statics/temp/"+file1+".jpg")
				os.remove("app/statics/temp/"+filename)
				filename=file1+".jpg"

			sig1,sig2 = Main.getSignatures("/home/carlos/Projects/line-recognition/app/statics/temp/"+filename)
			cv2.imwrite("app/statics/temp/"+g.user.username+"_"+file1+"1.png",sig1)
			cv2.imwrite("app/statics/temp/"+g.user.username+"_"+file1+"2.png",sig2)

			pathSrc= "/statics/temp/"+filename
			
			pathFile1="/statics/temp/"+g.user.username+"_"+file1+"1.png"
			pathFile2="/statics/temp/"+g.user.username+"_"+file1+"2.png"
			control="something"
			
	return render_template('user/home.html',**locals())


@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('welcome'))




app.register_blueprint(userModule)