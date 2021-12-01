from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from django.urls import reverse

from accounts.models import User

# Create your tests here.
class PaymentTest(APITestCase):
	def setUp(self):
		email = "venusaur@gmail.com"
		first_name = 'venu'
		last_name = 'saur'
		no_telepon = '0855313373133711'
		is_company = False
		username = "venusaur1i"
		password = "13371337"
		User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, no_telepon=no_telepon, is_company=is_company,  password=password)

		email = "venusaur3@gmail.com"
		first_name = 'venu'
		last_name = 'saur'
		no_telepon = '0855313373133713'
		is_company = True
		username = "venusaur1c"
		password = "13371337"
		User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, no_telepon=no_telepon, is_company=is_company,  password=password)

		self.api_authentication('venusaur1c', '13371337')

		data = {
			'title': 'this is title',
			'description': 'cool description',
			'fee': 1337
		}

		url = reverse('Campaign List Create')
		response = self.client.post(url, data, format='json')


		self.api_authentication('venusaur1i', '13371337')
		data = {
			'campaign_id': '1'
		}

		url = reverse('JoinCampaign List Create')
		response = self.client.post(url, data, format='json')

	def api_authentication(self, username, password):
		url = reverse('Token Obtain Pair')
		data = {
			'username': username,
			'password': password
		}
		response = self.client.post(url, data)
		self.jwt = response.data['access']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.jwt)

	def testPayment(self):
		data = {
			'joinCampaign_id': '1'
		}

		url = reverse('Payment Create')
		response = self.client.post(url, data, format='json')
		print(response.data)
