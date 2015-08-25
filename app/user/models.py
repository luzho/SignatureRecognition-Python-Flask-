# -*- encoding: utf-8 -*-
from app import db
from werkzeug import check_password_hash, generate_password_hash

class User(db.Model):
	__tablename__ = "users"
	__table_args__ = {'sqlite_autoincrement': True}
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), index=True, unique=True)
	email = db.Column(db.String(255), index=True, unique=True)
	password = db.Column(db.String(255))
	img_num = db.Column(db.Integer)

	def __init__(self , username ,password , email):
		self.username = username
		self.setPassword(password)
		self.email = email
		self.img_num = 0

	def setPassword(self, password):
		self.password = generate_password_hash(password)

	def checkPassword(self, password):
		return check_password_hash(self.password, password)	

	def __repr__(self):
		return '<User %r>' % (self.username)

	def is_authenticated(self):
		return True
	
	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)