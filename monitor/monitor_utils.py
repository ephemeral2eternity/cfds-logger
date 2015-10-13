from urllib.request import urlopen
from datetime import datetime
from monitor.models import client, leftClient

# ===========================================================================
# Check the availability of existing clients
# ===========================================================================
def check_client_availability():
	all_clients = client.objects.all()
	for cl in all_clients:
		check_url = "http://%s:8717/latest" % cl.ip
		print(check_url)
		print("[Client-INFO]Checking Client " + cl.name + " availability!")
		try:
			rsp = urlopen(check_url)
			cl.last_visit = datetime.now()
			cl.save()
		except:
			print("[Client-INFO]Client " + cl.name + " leaves the system!")
			num_results = leftClient.objects.filter(ip=cl.ip).count()
			if num_results > 0:
				cur_obj = leftClient.objects.filter(ip=cl.ip)[0]
				cur_obj.left_ts = datetime.now()
				cur_obj.save()
			else:
				left_cl = leftClient(name=cl.name, ip=cl.ip)
				left_cl.save()
			pass
