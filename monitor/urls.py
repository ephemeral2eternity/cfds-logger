from django.conf.urls import patterns, url
from monitor import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add', views.add, name='add'),
	url(r'^edge', views.add_link, name='edge'),
	url(r'^left/$', views.query_left_clients, name='left'),
	url(r'^empty_left/$', views.empty_left_clients, name='empty_left'),
	url(r'^empty_links/$', views.empty_links, name='empty_links'),
	url(r'^get_link_json/$', views.link_json, name='get_link_json'),
	url(r'^link_graph/$', views.link_graph, name='link_graph'),
)
