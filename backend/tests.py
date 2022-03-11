import unittest
from flask import current_app
from src import create_app
from src import db
from src.models import User, Posts
import re
import os

class TestBases(unittest.TestCase):
	def setUp(self):
		self.app = create_app(config_file='config.TestingConfig')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		self.client = self.app.test_client()
		
	def testappExists(self):
		self.assertNotEqual(current_app, None)
	
	def testEnvironment(self):
		self.assertEqual(current_app.config['ENV'], "Testing")
	
	def testDBexists(self):
		self.assertEqual(2, 2)
	
	def testUserEndpoints(self):
		response = self.client.get('/users/')
		self.assertEqual(response.status, '200 OK')
	
	def testpostsEndpoints(self):
		response = self.client.get('/posts/')
		self.assertEqual(response.status, '200 OK')
	
	def testUserCreation(self):
		pass
	
	def testPostCreation(self):
		pass
		
	def tearDown(self):
		os.unlink('test.sqlite')
		

if __name__ == '__main__':
	unittest.main()
