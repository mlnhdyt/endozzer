# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from django.urls import reverse

from accounts.models import *

import datetime

user_data_company = [
	{
		'email': 'company1@gmail.com',
		'username': 'company1',
		'first_name': 'compa',
		'last_name': 'ny',
		'no_telepon': '0855313373133711',
		'password': '13371337',
		'is_company': True
	},

	{
		'email': 'company2@gmail.com',
		'username': 'company2',
		'first_name': 'compa',
		'last_name': 'ny',
		'no_telepon': '0855313373133712',
		'password': '13371337',
		'is_company': True
	},
	{
		'email': 'company3@gmail.com',
		'username': 'company3',
		'first_name': 'compa',
		'last_name': 'ny',
		'no_telepon': '0855313373133713',
		'password': '13371337',
		'is_company': True
	},
]

user_data_influencer = [
	{
		'email': 'influencer1@gmail.com',
		'username': 'influencer1',
		'first_name': 'infl',
		'last_name': 'uencer',
		'domicile': 'akihabara',
		'no_telepon': '0855313373133721',
		'password': '13371337',
		'is_company': False
	},

	{
		'email': 'influencer2@gmail.com',
		'username': 'influencer2',
		'first_name': 'infl',
		'last_name': 'uencer',
		'domicile': 'akihabara',
		'no_telepon': '0855313373133722',
		'password': '13371337',
		'is_company': False
	},
	{
		'email': 'influencer3@gmail.com',
		'username': 'influencer3',
		'first_name': 'infl',
		'last_name': 'uencer',
		'domicile': 'akihabara',
		'no_telepon': '0855313373133723',
		'password': '13371337',
		'is_company': False
	},
]



class UserTest(APITestCase):

	def setUp(self):

		User.objects.create_user(username=user_data_influencer[0]['username'], email=user_data_influencer[0]['email'], first_name=user_data_influencer[0]['first_name'], domicile=user_data_influencer[0]['domicile'], last_name=user_data_influencer[0]['last_name'], no_telepon=user_data_influencer[0]['no_telepon'], is_company=user_data_influencer[0]['is_company'],  password=user_data_influencer[0]['password'])
		User.objects.create_user(username=user_data_influencer[1]['username'], email=user_data_influencer[1]['email'], first_name=user_data_influencer[1]['first_name'], domicile=user_data_influencer[1]['domicile'], last_name=user_data_influencer[1]['last_name'], no_telepon=user_data_influencer[1]['no_telepon'], is_company=user_data_influencer[1]['is_company'],  password=user_data_influencer[1]['password'])
		User.objects.create_user(username=user_data_influencer[2]['username'], email=user_data_influencer[1]['email'], first_name=user_data_influencer[2]['first_name'], domicile=user_data_influencer[2]['domicile'], last_name=user_data_influencer[2]['last_name'], no_telepon=user_data_influencer[2]['no_telepon'], is_company=user_data_influencer[2]['is_company'],  password=user_data_influencer[2]['password'])

		User.objects.create_user(username=user_data_company[0]['username'], email=user_data_company[0]['email'], first_name=user_data_company[0]['first_name'], last_name=user_data_company[0]['last_name'], domicile=user_data_influencer[0]['domicile'], no_telepon=user_data_company[0]['no_telepon'], is_company=user_data_company[0]['is_company'],  password=user_data_company[0]['password'])
		User.objects.create_user(username=user_data_company[1]['username'], email=user_data_company[1]['email'], first_name=user_data_company[1]['first_name'], last_name=user_data_company[1]['last_name'], domicile=user_data_influencer[1]['domicile'], no_telepon=user_data_company[1]['no_telepon'], is_company=user_data_company[1]['is_company'],  password=user_data_company[1]['password'])
		User.objects.create_user(username=user_data_company[2]['username'], email=user_data_company[1]['email'], first_name=user_data_company[2]['first_name'], last_name=user_data_company[2]['last_name'], domicile=user_data_influencer[2]['domicile'], no_telepon=user_data_company[2]['no_telepon'], is_company=user_data_company[2]['is_company'],  password=user_data_company[2]['password'])

	def api_authentication(self, username, password):
		url = reverse('Token Obtain Pair')
		data = {
			'username': username,
			'password': password
		}
		response = self.client.post(url, data)
		self.jwt = response.data['access']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.jwt)


	def test_influezer(self):

		for i in [1, 2, 3]:
			self.api_authentication(user_data_influencer[i-1]['username'], user_data_influencer[i-1]['password'])

			data = {
				'user_id': i,
				'birth_date': datetime.date.today(),
				'gender': 1,
			}
			url = reverse('Influenzer List Create')
			response = self.client.post(url, data)
			self.assertEqual(201, response.status_code)


		url = reverse('Influenzer Detail', kwargs={'pk': 1})
		response = self.client.get(url, data)
		self.assertEqual(200, response.status_code)

		data = {
			'domicile': 'osaka',
			'no_telepon': '0000000',
			'birth_date': datetime.date.today(),
			'gender': 1,
		}

		url = reverse('Influenzer Detail', kwargs={'pk': 1})
		response = self.client.patch(url, data)
		self.assertEqual(200, response.status_code)

		url = reverse('Influenzer List Create')
		response = self.client.get(url, data)
		self.assertEqual(200, response.status_code)

	def test_company(self):
		for i in [1, 2, 3]:
			self.api_authentication(user_data_company[1]['username'], user_data_company[1]['password'])

			data = {
				'user_id': i,
				'brand': 'liquid paradewa',
				'address': 'gatau apa ah',
			}
			url = reverse('Company Create')
			response = self.client.post(url, data)
			self.assertEqual(201, response.status_code)


		url = reverse('Company Detail', kwargs={'pk': 1})
		response = self.client.get(url, data)
		self.assertEqual(200, response.status_code)

		data = {
			'domicile': 'osaka',
			'brand': 'xxxxxxxxxxxxxxxxxx',
			'no_telepon': '1333333333333337'
		}


		url = reverse('Company Detail', kwargs={'pk': 1})
		response = self.client.patch(url, data)
		self.assertEqual(200, response.status_code)

