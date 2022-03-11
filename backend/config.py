import os


basedir = os.path.abspath(os.path.dirname(__file__))

class ProductionConfig:
	DEBUG = False
	TESTING = False
	ENV = "Production"
	SECRET_KEY = os.urandom(10)
	SQLALCHEMY_DATABASE_URI = os.path.join('sqlite:///'+ os.path.join(basedir, 'main.sqlite'))
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig:
	DEBUG = True
	TESTING = True
	ENV = "Testing"
	SQLALCHEMY_DATABASE_URI = os.path.join('sqlite:///'+ os.path.join(basedir, 'test.sqlite'))
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	
