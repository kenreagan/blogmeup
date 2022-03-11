from flask import Blueprint, jsonify
from flask.views import MethodView
from src.models import User, Posts
from werkzeug.security import generate_password_hash

api = Blueprint('api', __name__)

class ManagePosts(MethodView):
	def PUT(self):
		pass
	
	def GET(self):
		posts = Posts.query.all()
		empt = []
		for post in posts:
			empt.append(post.to_json())
		return jsonify({"users": empt})
		
	def DELETE(self):
		pass
	

class ManageUsers(MethodView):
	def PUT(self):
		pass
	
	def GET(self):
		user = User.query.all()
		empt = []
		for users in user:
			empt.append(users.to_json())
		return jsonify({"users": empt})
		
	def DELETE(self):
		pass
	
