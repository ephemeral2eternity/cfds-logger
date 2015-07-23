from django.db import models

# Create your models here.
class client(models.Model):
	name = models.CharField(max_length=20)
	ip = models.CharField(max_length=20)
	last_visit = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# Create your models here.
class leftClient(models.Model):
	name = models.CharField(max_length=20)
	ip = models.CharField(max_length=20)
	left_ts = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
