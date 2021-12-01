from django.db import models
from django.contrib.auth.models import AbstractUser
from addutils.models import PositiveBigIntegerField

# Create your models here.

class User(AbstractUser):
	domicile = models.CharField(max_length=20, null=True)
	no_telepon = models.CharField(max_length=20, default='-', unique=True)
	is_company = models.BooleanField(default=False)

class Influenzer(models.Model):
	GENDER_TYPES = (
		(0, 'None'),
		(1, 'Laki-laki'),
		(2, 'Perempuan')
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	birth_date = models.DateField()
	gender = models.PositiveSmallIntegerField(choices=GENDER_TYPES, default=0)
	instagram = models.CharField(max_length=20)
	tiktok = models.CharField(max_length=20)
	balance = PositiveBigIntegerField(default=0)

class Company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	brand = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
