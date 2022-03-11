from flask import Blueprint, jsonify, request
from flask.views import MethodView
from src.models import User, Posts
from werkzeug.security import generate_password_hash
from src import db

api = Blueprint('api', __name__)


@api.route('/users/post/<int:id>')
def getuserposts(id):
	posts = Posts.query.filter_by(author=id).all()
	empt = []
	for post in posts:
		empt.append(post.to_json())
		


class ManagePosts(MethodView):
	def put(self):
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
	
	def get(self):
		posts = Posts.query.all()
		empt = []
		for post in posts:
			empt.append(post.to_json())
		return {
			"posts": empt
		}
		
		
	def delete(self):
		data = dict(request.get_json())
		post = Posts.query.filter_by(id=data['id']).first()
		db.session.delete(post)
		db.session.commit()
		return {
			"Message": "Record Deletion success"
		}
		
	def post(self):
		data = dict(request.get_json())
		title = data['title']
		body = data['body']
		author = int(data['author'])
		post = Posts(title=title, body=body, author=author)
		db.session.add(post)
		db.session.commit()
		return {
			"Message": "Posts creation success"
		}
	
	

class ManageUsers(MethodView):
	def put(self):
		data = dict(request.get_json())
		user_id = data['id']
		username = data['name']
		user = User.query.filter_by(id=user_id).first()
		user.name = username
		db.session.commit()
		return {
			"message": "recorded update sucess" 
		}
	
	def get(self):
		user = User.query.all()
		empt = []
		for users in user:
			empt.append(users.to_json())
		return {
			"users": empt
		}
		
	def delete(self):
		data = dict(request.get_json())
		user = User.query.filter_by(id=data['id']).first()
		db.session.delete(user)
		db.session.commit()
		return {
			"Message": "Record Deletion success"
		}
	
	def post(self):
		data = dict(request.get_json())
		name = data['name']
		password = generate_password_hash(data['password'])
		user = User(name=name, password=password)
		db.session.add(user)
		db.session.commit()
		return {
			"Message": "User creation success"
		}
		
userinstance = ManageUsers.as_view('users')
postsinstance = ManagePosts.as_view('posts')
		
api.add_url_rule('/users/', view_func=userinstance)
api.add_url_rule('/posts/', view_func=postsinstance)

	
