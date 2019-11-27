from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User

from index.models import Post

class SimpleTest(TestCase):
	def test_home_page(self):
		response = self.client.get('/home/')
		self.assertEqual(response.status_code,200)

	def test_about_page(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code,200)

	def test_projects_page(self):
		response = self.client.get('/projects/')
		self.assertEqual(response.status_code,200)


	def test_contact_page(self):
		response = self.client.get('/contact/')
		self.assertEqual(response.status_code,200)


	def test_contact_page(self):
		response = self.client.get('/home/', args=['1'])
		self.assertEqual(response.status_code,200)
