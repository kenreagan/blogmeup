from src import db
from werkzeug.security import check_password_hash
import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	password = db.Column(db.String(200), nullable=False)
	## post created is a list storing posts created by user
	post_created = db.relationship('Posts', backref='posts', lazy='dynamic', cascade="all, delete-orphan")
	
	def __repr__(self):
		return '<%d: %s>'%(self.id, self.name)
	
	def to_json():
		return {
			"id": self.id,
			"name": self.name,
			"email": self.email
		}
	
	@staticmethod
	def authenticate(password)-> bool:
		return {
		 		"authenticate": check_password_hash(password)
		 	}

	
class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	body = db.Column(db.Text, nullable=False)
	date_created = db.Column(db.Date, default=datetime.datetime.utcnow)
	
	def __repr__(self):
		return '<%d: %s>'%(self.id, self.title)
	
	def _to_json():
		return {
			"id": self.id,
			"title": self.title,
			"body": self.body,
			"author": self.author
		}
