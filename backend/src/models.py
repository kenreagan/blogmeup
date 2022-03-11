from src import db
from werkzeug.security import check_password_hash

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	password = db.Column(db.String(200), nullable=False)
	## post created is a list storing posts created by user
	post_created = db.relationship('Posts', backref)
	
	def __repr__(self):
		return '<%d: %s>'%(self.id, self.name)
	
	def _to_json():
		return {
			"id": self.id,
			"name": self.name,
			"email": self.email
		}
	
	@staticmethod
	def authenticate(password)-> bool:
		return {
		 		"authemnticate": check_password_hash(password)
		 	}
	
class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	author = db.Column(db.Integer, db.ForeignKey('user))
	body = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return '<%d: %s>'%(self.id, self.title)
	
	def _to_json():
		return {
			"id": self.id,
			"title": self.title,
			"body": self.body,
			"author": self.author
		}
