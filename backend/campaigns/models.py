from django.db import models
from accounts.models import User

from .utils import join_img_upload, campaign_img_upload

from django.dispatch import receiver


class Campaign(models.Model):

	# GENDER_TYPE = (
	# 	(0, 'None'),
	# 	(1, 'Laki-laki'),
	# 	(2, 'Perempuan')
	# )

	# AGE_TYPE = (
	# 	(0, 'None'),
	# 	(1, '<18'),
	# 	(2, '18-24'),
	# 	(3, '25-34'),
	# 	(4, '35-49'),
	# 	(5, '>50'),

	# )

	# CATEGORY = (
	# 	(0, 'None'),
	# 	(1, 'Entertainment'),
	# 	(2, 'Family & Parenting'),
	# 	(3, 'Health & Sport'),
	# 	(4, 'Food & Baverages'),
	# 	(5, 'Lifestyle & Travel'),
	# 	(6, 'Beauty & Fashion'),
	# 	(7, 'Technology'),
	# 	(8, 'Gaming'),
	# )

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	category = models.CharField(max_length=50)
	img = models.ImageField(upload_to=campaign_img_upload, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	description = models.CharField(max_length=50)
	#
	gender = models.CharField(max_length=10)
	domicile = models.CharField(max_length=20)
	min_followers = models.IntegerField(default=0)
	desc_photo = models.CharField(max_length=100)
	example_photo = models.ImageField(upload_to=campaign_img_upload, blank=True)
	desc_caption = models.CharField(max_length=100)
	age = models.CharField(max_length=50)
	periode_start = models.DateTimeField()
	periode_end = models.DateTimeField()
	#

	fee = models.PositiveIntegerField(default=0)

	def set_age(self, x):
		self.age = json.dumps(x)

	def get_age(self):
		return json.loads(self.age)

	def set_gender(self, x):
		self.gender = json.dumps(x)

	def get_gender(self):
		return json.loads(self.gender)

	def set_category(self, x):
		self.category = json.dumps(x)

	def get_category(self):
		return json.loads(self.category)

	def __str__(self):
		return self.title

class JoinCampaign(models.Model):

	STATUS_TYPES = (
		(1, 'Menunggu Konfirmasi'),
		(2, 'Lolos Seleksi'),
		(3, 'Tidak Lolos Seleksi'),
		(4, 'Task Selesai')
	)

	DRAFT_STATUS_TYPES = (
		(1, 'Belum Upload'),
		(2, 'Baru'),
		(3, 'Ditolak'),
		(4, 'Diterima')
	)

	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.PositiveSmallIntegerField(choices=STATUS_TYPES, default=1)
	draft = models.ImageField(upload_to=join_img_upload, blank=True)
	draft_caption = models.CharField(max_length=1000)
	draft_status = models.PositiveSmallIntegerField(choices=DRAFT_STATUS_TYPES, default=1)
	post = models.ImageField(upload_to=join_img_upload, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


# class DraftPost(models.Model):
# 	joinCampaign = models.ForeignKey(JoinCampaign, on_delete=models.CASCADE)
# 	post = models.ImageField(upload_to=upload_to, blank=True)
# 	accepted = models.BooleanField(default=False)


# stakeholder
# kebijakan hukum
# hasil fgd
# kesimpulan
# kurang 
# dampak