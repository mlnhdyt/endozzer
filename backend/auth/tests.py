from rest_framework.test import APITestCase

from django.urls import reverse

from accounts.models import User


# class UserCreate(APITestCase):
# 	def test_create_company(self):
# 		url = reverse('Register')
# 		data = {
# 			'username' : 'venusaur',
# 			'password' : 'password123x',
# 			'password2' : 'password123x',
# 			'email' : 'venusaur@gmail.com',
# 			'first_name' : 'venu',
# 			'last_name' : 'saur',
# 			'no_telepon' : '08551337133711',
# 			'is_company' : 'true'
# 		}
# 		response = self.client.post(url, data, format='json')
# 		self.assertEqual(201, response.status_code)

# 	def test_create_influenzer(self):
# 		url = reverse('Register')
# 		data = {
# 			'username' : 'venusaur',
# 			'password' : 'password123x',
# 			'password2' : 'password123x',
# 			'email' : 'venusaur@gmail.com',
# 			'first_name' : 'venu',
# 			'last_name' : 'saur',
# 			'no_telepon' : '08551337133711',
# 			'is_company' : 'false'
# 		}
# 		response = self.client.post(url, data, format='json')
# 		self.assertEqual(201, response.status_code)

