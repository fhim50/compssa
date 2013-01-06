#from django.conf.urls.defaults import *
from django.conf.urls import url , patterns , include



urlpatterns = patterns('fileserver.views',
	url(r'^$', 'index'),
	url(r'^(?P<fileserver_name>.*?)/(?P<path>)$', 'directory'),
)