from flask import Flask
from flask_sqlalchemy import SQLALchemy

db = SQLALchemy()

def create_app(config_file):
	app = Flask(__name__)
	db.init_app(app)
	from src.views import api
	app.register_blueprint(api, url_prefix='/')
	return app
