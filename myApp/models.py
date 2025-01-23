from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=30, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.username