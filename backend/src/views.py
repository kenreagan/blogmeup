from flask import Blueprint, jsonify
from flask.views import MethodView
from src.models import User, Posts
from werkzeug.security import generate_password_hash
from src import db

api = Blueprint('api', __name__)

class ManagePosts(MethodView):
	def PUT(self):
		data = dict(request.get_json())
		post_id = data['id']
		title = data['title']
		body = data['body']
		author = data['author']
		post = Posts.query.filter_by(id=post_id).first()
		post.title = title
		post.body = body
		post.author = author
		db.session.commit()
		return {
			"message": "recorded update sucess" 
		}		
	
	def GET(self):
		posts = Posts.query.all()
		empt = []
		for post in posts:
			empt.append(post.to_json())
		return jsonify({"posts": empt})
		
		
	def DELETE(self):
		data = dict(request.get_json())
		post = Posts.query.filter_by(id=data['id']).first()
		db.session.delete(post)
		db.session.commit()
		return {
			"Message": "Record Deletion success"
		}
	

class ManageUsers(MethodView):
	def PUT(self):
		data = dict(request.get_json())
		user_id = data['id']
		username = data['name']
		email = data['email']
		user = User.query.filter_by(id=user_id).first()
		user.name = username
		user.email = email
		db.session.commit()
		return {
			"message": "recorded update sucess" 
		}
	
	def GET(self):
		user = User.query.all()
		empt = []
		for users in user:
			empt.append(users.to_json())
		return jsonify({"users": empt})
		
	def DELETE(self):
		data = dict(request.get_json())
		user = User.query.filter_by(id=data['id']).first()
		db.session.delete(user)
		db.session.commit()
		return {
			"Message": "Record Deletion success"
		}

userinstance = ManageUsers.as_view('users')
postsinstance = ManagePosts.as_view('posts')
		
api.add_url_rule('/users/', view_func=userinstance, methods=['GET', 'POST', 'DELETE', 'PUT'])
api.add_url_rule('/posts/', view_func=postsinstance, methods=['GET', 'POST', 'DELETE', 'PUT'])

	
