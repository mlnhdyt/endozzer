from django.db import models
from accounts.models import User

class Campaign(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	judul = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deskripsi = models.CharField(max_length=50)
	lunas = models.BooleanField(default=False)
	fee = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.judul

class JoinCampaign(models.Model):

	STATUS_TYPES = (
		(1, 'Menunggu Konfirmasi'),
		(2, 'Lolos Seleksi'),
		(3, 'Tidak Lolos Seleksi'),
		(4, 'Task Selesai')
	)

	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.PositiveSmallIntegerField(choices=STATUS_TYPES, default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
