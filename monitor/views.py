from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from monitor.models import client, leftClient, link
from django.http import HttpResponse
from django.http import JsonResponse
import socket
import json
import urllib

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
	left_client_list = leftClient.objects.all().order_by('-left_ts')
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

@csrf_exempt
def empty_left_clients(request):
	leftClient.objects.all().delete()
	response = HttpResponse("Successfully empty the leaving clients record!!!")
	return response

@csrf_exempt
def empty_links(request):
	link.objects.all().delete()
	response = HttpResponse("Successfully empty all the recorded links!")
	return response

@csrf_exempt
def add_link(request):
	url = request.get_full_path()
	params = url.split('?')[1]
	update_dict = urllib.parse.parse_qs(params)
	if 'src' in update_dict.keys():
		src_client = update_dict['src'][0]
		num_rsts = client.objects.filter(name=src_client).count()
		if num_rsts < 1:
			src_client_ip = socket.gethostbyaddr(src_client)[0]
			new_client = client(name=src_client, ip=src_client_ip)
			new_client.save()
		src_client_id = client.objects.filter(name=src_client)[0].id
		if 'pdst' in update_dict.keys():
			dst_client = update_dict['pdst'][0]
			num_rsts = client.objects.filter(name=dst_client).count()
			if num_rsts < 1:
				dst_client_ip = socket.gethostbyaddr(dst_client)[0]
				new_client = client(name=dst_client, ip=dst_client_ip)
				new_client.save()
			dst_client_id = client.objects.filter(name=dst_client)[0].id
			plink = link(src=src_client, src_id=src_client_id, dst=dst_client, dst_id=dst_client_id, link_type=0)
			plink.save()
		if 'vdst' in update_dict.keys():
			dst_client = update_dict['vdst'][0]
			num_rsts = client.objects.filter(name=dst_client).count()
			if num_rsts < 1:
				dst_client_ip = socket.gethostbyaddr(dst_client)[0]
				new_client = client(name=dst_client, ip=dst_client_ip)
				new_client.save()
			dst_client_id = client.objects.filter(name=dst_client)[0].id
			vlink = link(src=src_client, src_id=src_client_id, dst=dst_client, dst_id=dst_client_id, link_type=1)
			vlink.save()
		response = HttpResponse("Successfully add links for source client: " + src_client)
	else:
		response = HttpResponse("An monitor/edge? request needs to concatenate with src=src_name&pdst=pdst_name&vdst=vdst_name!!")
	return response

# Show the link graph for all clients in D3.js
def link_graph(request):
	return render_to_response("monitor/link_graph.html")

@csrf_exempt
def link_json(request):
	all_links = link.objects.order_by('-ts')[:100]
	link_list = []
	for lk in all_links:
		cur_link = {}
		cur_link['source'] = lk.src
		cur_link['target'] = lk.dst
		cur_link['value'] = lk.link_type
		link_list.append(cur_link)
	link_json = {}
	link_json['links'] = link_list
	return JsonResponse(link_json, safe=False)
