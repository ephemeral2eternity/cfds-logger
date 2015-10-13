from django.db import models

# The connected clients.
class client(models.Model):
	name = models.CharField(max_length=20)
	ip = models.CharField(max_length=20)
	last_visit = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# The leaving clients.
class leftClient(models.Model):
	name = models.CharField(max_length=20)
	ip = models.CharField(max_length=20)
	left_ts = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# Record recent communications between clients
class link(models.Model):
	src = models.CharField(max_length=20)
	src_id = models.IntegerField()
	dst = models.CharField(max_length=20)
	dst_id = models.IntegerField()
	link_type = models.IntegerField()
	ts = models.DateTimeField(auto_now=True)
	def __str__(self):
		return src + "<---->" + dst
