from django.conf.urls import patterns, include, url
from django.conf import settings
import forum
import fileserver
from register.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    # Examples:
    # url(r'^$', 'compassa_reg.views.home', name='home'),
    #url(r'^compassa_reg/', include('compassa_reg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^forum/', include('forum.urls')),
	url(r'^accounts/', include('registration.urls')),
	#url(r'^accounts/', include('Accounts.urls'))
	url(r'^home/', 'register.views.home'),
	url(r'files/', include('fileserver.urls')),
	
)
