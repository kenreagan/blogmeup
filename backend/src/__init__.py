from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_file):
	app = Flask(__name__)
	app.config.from_object(config_file)
	db.init_app(app)
	from src.views import api
	app.register_blueprint(api, url_prefix='/')
	return app
