# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from django.urls import reverse

from accounts.models import User

import io
from PIL import Image

from .models import *
from django.utils import timezone
############
# Todo: create test untuk akun influencer
############

	# gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE, default=0)
	# domicile = models.CharField(max_length=20)
	# min_followers = models.IntegerField(default=0)
	# desc_photo = models.CharField(max_length=100)
	# example_photo = models.ImageField(upload_to=campaign_img_upload, blank=True)
	# desc_caption = models.CharField(max_length=100)
	# age = models.CharField(max_length=50)

campaign_data = [
	{
		'title': 'this is title',
		'description': 'cool description',
		'fee': 1337,
		'gender': '[1]',
		'domicile': 'osaka',
		'min_followers': 0,
		'desc_photo': 'xxxxx',
		'desc_caption': 'askdlasdk',
		'age': '[1,2,3]',
		'category': '[5, 6, 7]',
		'periode_start': timezone.now().replace(hour=0, minute=0, second=0, microsecond=0),
		'periode_end': timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) +  timezone.timedelta(1)
	},
	{
		'title': 'another title',
		'description': 'another cool description',
		'fee': 0xdead,
		'gender': '[1, 2]',
		'domicile': 'osaka',
		'min_followers': 0,
		'desc_photo': 'xxxxx',
		'desc_caption': 'askdlasdk',
		'age': '[1,2,3]',
		'category': '[5, 6, 7]',
		'periode_start': timezone.now().replace(hour=0, minute=0, second=0, microsecond=0),
		'periode_end': timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) +  timezone.timedelta(2)
	}
]

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
		'no_telepon': '0855313373133721',
		'password': '13371337',
		'is_company': False
	},

	{
		'email': 'influencer2@gmail.com',
		'username': 'influencer2',
		'first_name': 'infl',
		'last_name': 'uencer',
		'no_telepon': '0855313373133722',
		'password': '13371337',
		'is_company': False
	},
	{
		'email': 'influencer3@gmail.com',
		'username': 'influencer3',
		'first_name': 'infl',
		'last_name': 'uencer',
		'no_telepon': '0855313373133723',
		'password': '13371337',
		'is_company': False
	},
]


# class CampaignTest(APITestCase):
# 	def setUp(self):

# 		User.objects.create_user(username=user_data_company[0]['username'], email=user_data_company[0]['email'], first_name=user_data_company[0]['first_name'], last_name=user_data_company[0]['last_name'], no_telepon=user_data_company[0]['no_telepon'], is_company=user_data_company[0]['is_company'],  password=user_data_company[0]['password'])
# 		User.objects.create_user(username=user_data_company[1]['username'], email=user_data_company[1]['email'], first_name=user_data_company[1]['first_name'], last_name=user_data_company[1]['last_name'], no_telepon=user_data_company[1]['no_telepon'], is_company=user_data_company[1]['is_company'],  password=user_data_company[1]['password'])
# 		User.objects.create_user(username=user_data_influencer[0]['username'], email=user_data_influencer[0]['email'], first_name=user_data_influencer[0]['first_name'], last_name=user_data_influencer[0]['last_name'], no_telepon=user_data_influencer[0]['no_telepon'], is_company=user_data_influencer[0]['is_company'],  password=user_data_influencer[0]['password'])

# 		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])

# 	def api_authentication(self, username, password):
# 		url = reverse('Token Obtain Pair')
# 		data = {
# 			'username': username,
# 			'password': password
# 		}
# 		response = self.client.post(url, data)
# 		self.jwt = response.data['access']
# 		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.jwt)

# 	# def generate_photo_file(self):
# 	# 	file = io.BytesIO()
# 	# 	image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
# 	# 	image.save(file, 'png')
# 	# 	file.name = 'test.png'
# 	# 	file.seek(0)
# 	# 	return file

# 	def create_campaign(self, data):
# 		url = reverse('Campaign List Create')
# 		return self.client.post(url, data, format='json')

# 	def test_create_campaign(self):
# 		response = self.create_campaign(data=campaign_data[0])
# 		self.assertEqual(201, response.status_code)

# 	def test_list_campaign(self):
# 		self.create_campaign(data=campaign_data[0])
# 		self.create_campaign(data=campaign_data[1])

# 		url = reverse('Campaign List Create')
# 		response = self.client.get(url, format='json')

# 		self.assertEqual(2, len(response.data))
# 		self.assertEqual("this is title", response.data[0]['title'])
# 		self.assertEqual("another title", response.data[1]['title'])

# 	def test_list_check_permission(self):
# 		self.create_campaign(data=campaign_data[0])

# 		url = reverse('Campaign List Create')
# 		response = self.client.get(url, format='json')
# 		self.assertEqual('this is title', response.data[0]['title'])

# 		self.api_authentication(user_data_company[1]['username'], user_data_company[1]['password'])
# 		response = self.client.get(url, format='json')
# 		self.assertEqual([], response.data)

# 		# influencer check list
# 		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
# 		response = self.client.get(url, format='json')
# 		self.assertEqual(1, len(response.data))


# 	def test_detail_campaign(self):

# 		self.create_campaign(data=campaign_data[0])
# 		self.create_campaign(data=campaign_data[1])

# 		# retrieve
# 		url = reverse('Campaign Detail', kwargs={'pk': 1})
# 		response = self.client.get(url, format='json')
# 		print(response.data)
# 		self.assertEqual('this is title', response.data['title'])

# 		url = reverse('Campaign Detail', kwargs={'pk': 2})
# 		response = self.client.get(url, format='json')
# 		self.assertEqual('another title', response.data['title'])

# 		url = reverse('Campaign Detail', kwargs={'pk': 3})
# 		response = self.client.get(url, format='json')
# 		self.assertEqual(404, response.status_code)

# 		# update
# 		data = {
# 			'title': 'changed title'
# 		}

# 		url = reverse('Campaign Detail', kwargs={'pk': 1})
# 		response = self.client.patch(url, data=data, format='json')
# 		self.assertEqual(200, response.status_code)

# 		response = self.client.get(url, format='json')
# 		self.assertEqual('changed title', response.data['title'])

# 		# delete
# 		response = self.client.delete(url, format='json')
# 		self.assertEqual(204, response.status_code)

# 		response = self.client.get(url, format='json')
# 		self.assertEqual(404, response.status_code)

# 	def test_date(self):
# 		data = campaign_data[1]
# 		data['periode_start'] = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) +  timezone.timedelta(1)
# 		self.create_campaign(data=campaign_data[0])
# 		self.create_campaign(data=data)

# 		# influencer check list
# 		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
# 		url = reverse('Campaign List Create')
# 		response = self.client.get(url, format='json')
# 		print(response.data)
# 		self.assertEqual(1, len(response.data))


# 		url = reverse('Campaign Detail', kwargs={'pk': 2})
# 		response = self.client.get(url, format='json')
# 		print(response.data)
# 		self.assertEqual(404, response.status_code)

# 	def test_retrieve_permission(self):
# 		self.create_campaign(data=campaign_data[0])
# 		self.api_authentication(user_data_company[1]['username'], user_data_company[1]['password'])

# 		url = reverse('Campaign Detail', kwargs={'pk': 1})

# 		response = self.client.get(url, format='json')
# 		self.assertEqual(403, response.status_code)

# 		data = {
# 			'title': 'changed title'
# 		}

# 		response = self.client.patch(url, data=data, format='json')
# 		self.assertEqual(403, response.status_code)

# 		response = self.client.delete(url, format='json')
# 		self.assertEqual(403, response.status_code)


class JoinCampaignTest(APITestCase):
	def setUp(self):
		User.objects.create_user(username=user_data_influencer[0]['username'], email=user_data_influencer[0]['email'], first_name=user_data_influencer[0]['first_name'], last_name=user_data_influencer[0]['last_name'], no_telepon=user_data_influencer[0]['no_telepon'], is_company=user_data_influencer[0]['is_company'],  password=user_data_influencer[0]['password'])
		User.objects.create_user(username=user_data_influencer[1]['username'], email=user_data_influencer[1]['email'], first_name=user_data_influencer[1]['first_name'], last_name=user_data_influencer[1]['last_name'], no_telepon=user_data_influencer[1]['no_telepon'], is_company=user_data_influencer[1]['is_company'],  password=user_data_influencer[1]['password'])
		User.objects.create_user(username=user_data_company[0]['username'], email=user_data_company[0]['email'], first_name=user_data_company[0]['first_name'], last_name=user_data_company[0]['last_name'], no_telepon=user_data_company[0]['no_telepon'], is_company=user_data_company[0]['is_company'],  password=user_data_company[0]['password'])
		User.objects.create_user(username=user_data_company[1]['username'], email=user_data_company[1]['email'], first_name=user_data_company[1]['first_name'], last_name=user_data_company[1]['last_name'], no_telepon=user_data_company[1]['no_telepon'], is_company=user_data_company[1]['is_company'],  password=user_data_company[1]['password'])

		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])

		url = reverse('Campaign List Create')
		self.client.post(url, campaign_data[0], format='json')


	def api_authentication(self, username, password):
		url = reverse('Token Obtain Pair')
		data = {
			'username': username,
			'password': password
		}
		response = self.client.post(url, data)
		self.jwt = response.data['access']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.jwt)
	def generate_photo_file(self):
		file = io.BytesIO()
		image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
		image.save(file, 'png')
		file.name = 'test.png'
		file.seek(0)
		return file

	def test_createlist_joincampaign(self):
		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])

		# join campaign
		data = {
			'campaign_id': 1
		}
		url = reverse('JoinCampaign List Create')
		response = self.client.post(url, data, format='json')
		self.assertEqual(201, response.status_code)

		# list campaign
		response = self.client.get(url, format='json')
		self.assertEqual(1, len(response.data))

		# check permission list
		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
		response = self.client.get(url, format='json')
		self.assertEqual(1, len(response.data))

		self.api_authentication(user_data_company[1]['username'], user_data_company[1]['password'])
		response = self.client.get(url, format='json')
		self.assertEqual(0, len(response.data))

		self.api_authentication(user_data_influencer[1]['username'], user_data_influencer[1]['password'])

		# join campaign
		data = {
			'campaign_id': 1
		}
		url = reverse('JoinCampaign List Create')
		response = self.client.post(url, data, format='json')
		self.assertEqual(201, response.status_code)

		response = self.client.get(url, format='json')
		self.assertEqual(1, len(response.data))

		# check permission list
		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
		response = self.client.get(url, format='json')
		self.assertEqual(2, len(response.data))


	def test_detail_joincampaign(self):
		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])

		# join campaign
		data = {
			'campaign_id': 1
		}
		url = reverse('JoinCampaign List Create')
		self.client.post(url, data, format='json')

		# check detail
		url = reverse('JoinCampaign Detail', kwargs={'pk':1})
		response = self.client.get(url, format='json')
		self.assertEqual(1, response.data['campaign_id'])
		self.assertEqual(1, response.data['pk'])

		# check join campaign that doesnt exists
		url = reverse('JoinCampaign Detail', kwargs={'pk':2})
		response = self.client.get(url, format='json')
		self.assertEqual(404, response.status_code)

		# join campaign influencer 2
		self.api_authentication(user_data_influencer[1]['username'], user_data_influencer[1]['password'])
		url = reverse('JoinCampaign List Create')
		self.client.post(url, data, format='json')

		# check detail join campaign 2
		url = reverse('JoinCampaign Detail', kwargs={'pk':2})
		response = self.client.get(url, format='json')
		self.assertEqual(1, response.data['campaign_id'])
		self.assertEqual(2, response.data['pk'])

		# check permission
		url = reverse('JoinCampaign Detail', kwargs={'pk':1})
		response = self.client.get(url, format='json')
		self.assertEqual(403, response.status_code)

		# check detail
		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
		url = reverse('JoinCampaign Detail', kwargs={'pk':1})
		response = self.client.get(url, format='json')
		self.assertEqual(1, response.data['campaign_id'])

		# check permission
		url = reverse('JoinCampaign Detail', kwargs={'pk':2})
		response = self.client.get(url, format='json')
		self.assertEqual(403, response.status_code)

		self.api_authentication(user_data_company[1]['username'], user_data_company[1]['password'])

		url = reverse('JoinCampaign Detail', kwargs={'pk':1})
		response = self.client.get(url, format='json')
		self.assertEqual(403, response.status_code)

		url = reverse('JoinCampaign Detail', kwargs={'pk':2})
		response = self.client.get(url, format='json')
		self.assertEqual(403, response.status_code)

		# check join campaign that doesnt exist
		url = reverse('JoinCampaign Detail', kwargs={'pk':3})
		response = self.client.get(url, format='json')
		self.assertEqual(404, response.status_code)

	def testDate(self):
		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
		data = campaign_data[1]
		data['periode_end'] = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timezone.timedelta(1)
		# self.create_campaign()
		url = reverse('Campaign List Create')
		self.client.post(url, data, format='json')


		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])

		data = {
			'campaign_id': 2
		}
		url = reverse('JoinCampaign List Create')
		response = self.client.post(url, data, format='json')
		print(response.data)
		self.assertEqual(400, response.status_code)



# class DraftPostTest(APITestCase):

# 	def setUp(self):

# 		User.objects.create_user(username=user_data_influencer[0]['username'], email=user_data_influencer[0]['email'], first_name=user_data_influencer[0]['first_name'], last_name=user_data_influencer[0]['last_name'], no_telepon=user_data_influencer[0]['no_telepon'], is_company=user_data_influencer[0]['is_company'],  password=user_data_influencer[0]['password'])
# 		User.objects.create_user(username=user_data_influencer[1]['username'], email=user_data_influencer[1]['email'], first_name=user_data_influencer[1]['first_name'], last_name=user_data_influencer[1]['last_name'], no_telepon=user_data_influencer[1]['no_telepon'], is_company=user_data_influencer[1]['is_company'],  password=user_data_influencer[1]['password'])
# 		User.objects.create_user(username=user_data_company[0]['username'], email=user_data_company[0]['email'], first_name=user_data_company[0]['first_name'], last_name=user_data_company[0]['last_name'], no_telepon=user_data_company[0]['no_telepon'], is_company=user_data_company[0]['is_company'],  password=user_data_company[0]['password'])

# 		for i in [1, 2]:
# 			self.api_authentication(user_data_influencer[i-1]['username'], user_data_influencer[i-1]['password'])

# 			data = {
# 				'user_id': i,
# 				'birth_date': timezone.now(),
# 				'gender': 1,
# 			}
# 			url = reverse('Influenzer List Create')
# 			response = self.client.post(url, data)


# 		# create campaign
# 		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
# 		url = reverse('Campaign List Create')
# 		response = self.client.post(url, campaign_data[0], format='json')

# 		# join campaign influencer 1
# 		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
# 		data = {
# 			'campaign_id': '1'
# 		}
# 		url = reverse('JoinCampaign List Create')
# 		response = self.client.post(url, data, format='json')

# 		# join campaign influencer 2
# 		self.api_authentication(user_data_influencer[1]['username'], user_data_influencer[1]['password'])
# 		url = reverse('JoinCampaign List Create')
# 		response = self.client.post(url, data, format='json')

# 	def api_authentication(self, username, password):
# 		url = reverse('Token Obtain Pair')
# 		data = {
# 			'username': username,
# 			'password': password
# 		}
# 		response = self.client.post(url, data)
# 		self.jwt = response.data['access']
# 		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.jwt)

# 	def generate_photo_file(self):
# 		file = io.BytesIO()
# 		image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
# 		image.save(file, 'png')
# 		file.name = 'test.png'
# 		file.seek(0)
# 		return file

# 	def testUploadImg(self):
# 		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
# 		photo_file = self.generate_photo_file()
# 		data = {
# 			'img': photo_file
# 		}
# 		url = reverse('Img Create', kwargs={'pk': 1})
# 		response = self.client.patch(url, data, format='multipart')
# 		self.assertEqual(200, response.status_code)

# 	def testUploadExample(self):
# 		self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
# 		photo_file = self.generate_photo_file()
# 		data = {
# 			'example_photo': photo_file
# 		}
# 		url = reverse('Example Create', kwargs={'pk': 1})
# 		response = self.client.patch(url, data, format='multipart')
# 		self.assertEqual(200, response.status_code)

# 	def testDraftCaption(self):
# 		self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])

# 		data = {
# 			'draft_caption': 'aaaaa'
# 		}

# 		url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
# 		response = self.client.patch(url, data)
# 		print(response.data)



	# def testUpload(self):

	# 	# chek initial draft & post status value
	# 	self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	self.assertEqual(None, response.data['draft'])
	# 	self.assertEqual(None, response.data['post'])

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'draft': photo_file
	# 	}

	# 	# check permission
	# 	self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
	# 	url = reverse('Draft Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(400, response.status_code)

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'draft': photo_file
	# 	}

	# 	url = reverse('Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(400, response.status_code)

	# 	data = {
	# 		'joinCampaign_id': 1
	# 	}

	# 	self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])

	# 	url = reverse('Payment Create')
	# 	response = self.client.post(url, data, format='json')
	# 	print(response.data)

	# 	url = reverse('Payment Create')
	# 	response = self.client.post(url, data, format='json')
	# 	input()

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'draft': photo_file
	# 	}

	# 	self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])

	# 	url = reverse('Draft Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(400, response.status_code)

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	data = {
	# 		'status' : 2
	# 	}
	# 	response = self.client.patch(url, data, format='json')
	# 	self.assertEqual(2, response.data['status'])

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'draft': photo_file
	# 	}
		
	# 	self.api_authentication(user_data_influencer[1]['username'], user_data_influencer[1]['password'])
	# 	url = reverse('Draft Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(403, response.status_code)

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'draft': photo_file
	# 	}
	# 	self.api_authentication(user_data_influencer[0]['username'], user_data_influencer[0]['password'])
	# 	url = reverse('Draft Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(200, response.status_code)

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	self.assertEqual(2, response.data['draft_status'])

	# 	self.api_authentication(user_data_company[0]['username'], user_data_company[0]['password'])
	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	data = {
	# 		'draft_status' : 3
	# 	}
	# 	response = self.client.patch(url, data, format='json')
	# 	self.assertEqual(3, response.data['draft_status'])

	# 	photo_file = self.generate_photo_file()

	# 	data = {
	# 		'draft': photo_file
	# 	}
	# 	url = reverse('Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(400, response.status_code)

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	data = {
	# 		'draft_status' : 4
	# 	}
	# 	response = self.client.patch(url, data, format='json')
	# 	self.assertEqual(4, response.data['draft_status'])

	# 	photo_file = self.generate_photo_file()
	# 	data = {
	# 		'post': photo_file
	# 	}

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	self.assertEqual(None, response.data['post'])

	# 	url = reverse('Post Create', kwargs={'pk': 1})
	# 	response = self.client.patch(url, data, format='multipart')
	# 	self.assertEqual(200, response.status_code)

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	self.assertNotEqual(None, response.data['post'])

	# 	url = reverse('JoinCampaign Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	self.assertEqual(4, response.data['status'])

	# 	url = reverse('JoinCampaign List Create')
	# 	response = self.client.get(url, format='json')

	# 	url = reverse('Influenzer Detail', kwargs={'pk': 1})
	# 	response = self.client.get(url, format='json')
	# 	print(response.data)



