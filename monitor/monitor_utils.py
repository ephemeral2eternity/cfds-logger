import urllib2
from datetime import datetime
from monitor.models import client

# ===========================================================================
# Check the availability of existing clients
# ===========================================================================
def check_client_availability():
	clients = client.objects.all()
	for cl in clients:
		check_url = "http://%s:8717/latest" % cl.ip
		try:
			rsp = urllib2.urlopen(update_url)
			cl.last_visit = datetime.now()
			cl.save()
		except:
			print("[Client-INFO]Client " + cl.name + "leaves the system!")
			left_cl = leftClient(name=cl.name, ip=cl.ip)
			cl.delete()
			left_cl.save()
