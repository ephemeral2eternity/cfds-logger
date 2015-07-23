from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from monitor.models import client, leftClient
from django.http import HttpResponse
import socket

# Create your views here.
def index(request):
	local_host = str(socket.gethostname())
	client_list = client.objects.all()
	client_num = client_list.count()
	template = loader.get_template('monitor/clients.html')
	context = RequestContext(request, {
					'cur_host':local_host,
					'clients' : client_list,
					'client_num' : client_num,
	})
	return HttpResponse(template.render(context))

# Create your views here.
def query_left_clients(request):
	local_host = str(socket.gethostname())
	left_client_list = leftClient.objects.all()
	left_client_num = left_client_list.count()
	template = loader.get_template('monitor/left_clients.html')
	context = RequestContext(request, {
					'cur_host':local_host,
					'left_clients' : left_client_list,
					'left_client_num' : left_client_num,
	})
	return HttpResponse(template.render(context))

@csrf_exempt
def add(request):
	client_ip = request.META['REMOTE_ADDR']
	url = request.get_full_path()
	if '?' in url:
		client_name = url.split('?')[1]
	else:
		client_name = request.META['REMOTE_HOST']
	num_results = client.objects.filter(ip=client_ip).count()
	if num_results > 0:
		cur_client = client.objects.filter(ip=client_ip)[0]
		cur_client.name = client_name
	else:
		cur_client = client(name=client_name, ip=client_ip)
	cur_client.save()
	# Return successfully added response
	response = HttpResponse("Successfully add/update client: " + client_name)
	return response
