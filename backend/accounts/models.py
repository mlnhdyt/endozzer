from django.db import models
from django.contrib.auth.models import AbstractUser
from addutils.models import PositiveBigIntegerField

# Create your models here.

class User(AbstractUser):
	no_telepon = models.CharField(max_length=20, default='-', unique=True)
	saldo = PositiveBigIntegerField(default=0)
	is_company = models.BooleanField(default=False)

class Influenzer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	tanggalLahir = models.DateField()

class Company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	alamat = models.CharField(max_length=50)
