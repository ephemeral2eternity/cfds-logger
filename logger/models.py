from django.db import models

# The messages of various faults in the system
class msg(models.Model):
	client = models.CharField(max_length=20)
	node = models.CharField(max_length=20)
	video = models.IntegerField()
	qoe = models.DecimalField(max_digits=6, decimal_places=4, default=-1.0)
	msg = models.CharField(max_length=200)
	msg_type = models.IntegerField()
	ts = models.DateTimeField(auto_now=True)
	def __str__(self):
		return msg

# The messages of various faults in the system
class rMSG(models.Model):
	client = models.CharField(max_length=20)
	faulty_node = models.CharField(max_length=20)
	recovery_node = models.CharField(max_length=20)
	recovery_peer = models.CharField(max_length=20)
	qoe = models.DecimalField(max_digits=6, decimal_places=4, default=-1.0)
	recovery_qoe = models.DecimalField(max_digits=6, decimal_places=4, default=-1.0)
	video = models.IntegerField()
	recovery_time = models.DecimalField(max_digits=6, decimal_places=4)
	msg = models.CharField(max_length=200)
	msg_type = models.IntegerField()
	ts = models.DateTimeField(auto_now=True)
	def __str__(self):
		return msg
