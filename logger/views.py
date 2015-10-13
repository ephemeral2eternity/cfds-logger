from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import JsonResponse
from logger.models import msg, rMSG
import urllib
import json

# Show the recent faulty messages logging in the cfds-logger.
def index(request):
	msgs = msg.objects.order_by('-ts')[:100]
	template = loader.get_template('logger/msgs.html')
	context = RequestContext(request, {
				'msgs':msgs,
	})
	return HttpResponse(template.render(context))

# Show the recent recovery messages logging in the cfds-logger.
def viewRMSG(request):
	rmsgs = rMSG.objects.order_by('-ts')[:100]
	template = loader.get_template('logger/rmsgs.html')
	context = RequestContext(request, {
				'rmsgs':rmsgs,
	})
	return HttpResponse(template.render(context))

# Add new logged events into the existing logger
def add(request):
	url = request.get_full_path()
	if '?' in url:
		msg_dict_str = url.split('?')[1]
		msg_dict = urllib.parse.parse_qs(msg_dict_str)
		print(msg_dict)
		new_msg = msg(client=msg_dict['client'][0], node=msg_dict['node'][0], video=int(msg_dict['video'][0]), qoe=float(msg_dict['qoe'][0]), msg=msg_dict['msg'][0], msg_type=int(msg_dict['msg_type'][0]))
		new_msg.save()
		rsp_str = "Successfully add a fault message in the cfds-logger!"
	else:
		rsp_str = "The URL of adding MSG request is not correct, please check the format!"
	response = HttpResponse(rsp_str)
	return response

# Add new logged events into the existing logger
def addRMSG(request):
	url = request.get_full_path()
	print("This is addRMSG function!")
	if '?' in url:
		rmsg_dict_str = url.split('?')[1]
		rmsg_dict = urllib.parse.parse_qs(rmsg_dict_str)
		print(rmsg_dict)
		new_rmsg = rMSG(client=rmsg_dict['client'][0], faulty_node=rmsg_dict['faulty_node'][0], recovery_node=rmsg_dict['recovery_node'][0], recovery_peer=rmsg_dict['recovery_peer'][0], qoe=float(rmsg_dict['qoe'][0]), recovery_qoe=float(rmsg_dict['recovery_qoe'][0]), video=int(rmsg_dict['video'][0]), recovery_time=float(rmsg_dict['recovery_time'][0]), msg=rmsg_dict['msg'][0], msg_type=int(rmsg_dict['msg_type'][0]))
		new_rmsg.save()
		rsp_str = "Successfully add a fault message in the cfds-logger!"
	else:
		rsp_str = "The URL of adding rMSG request is not correct, please check the format of input recovery_msg_obj in the url encoding!"
	response = HttpResponse(rsp_str)
	return response
