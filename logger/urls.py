from django.conf.urls import patterns, url
from logger import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add', views.add, name='add'),
	url(r'^view_rmsg/$', views.viewRMSG, name='view_rmsg'),
	url(r'^rmsg', views.addRMSG, name='add_rmsg'),
)
