from django.conf.urls import patterns, url
from monitor import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add', views.add, name='add'),
	url(r'^left/$', views.query_left_clients, name='left'),
)
