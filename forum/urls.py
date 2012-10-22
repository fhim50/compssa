from django.conf.urls import url , patterns , include
from django.conf.urls.defaults import *
from forum.models import *
#from forum.views import *

urlpatterns = patterns('forum.views',
    ##url(r'^logout/$', 'Accounts.views.logout'),
    #url(r'^login/$', 'Accounts.views.login'), 
    #url(r'^register/$', 'Accounts.views.register'),
    #url(r'^/?next=/$', 'Accounts.views.login'), 
	url(r'^main','main' ),
	url(r'^forum/(\d+)/$','forum'),
	url(r'^thread/(\d+)/$', 'thread'),
	url(r'^post/(new_thread|reply)/(\d+)/$', 'post'),
	url(r"^reply/(\d+)/$", "reply"),
	url(r"^new_thread/(\d+)/$", "new_thread"),
	url(r"^profile/(\d+)/$", "profile"),
)
'''
url_patterns = patterns("",
	url(r'^main','forum.views.main' ),
	#url(r'^forum/(\d+)/$','forum.views.forum'),
	#url(r'^thread/(\d+)/$', 'forum.views.thread'),
	



)

urlpatterns = patterns('compassa_reg.forum.views'',
    ##url(r'^logout/$', 'Accounts.views.logout'),
    #url(r'^login/$', 'Accounts.views.login'), 
    #url(r'^register/$', 'Accounts.views.register'),
    #url(r'^/?next=/$', 'Accounts.views.login'), 
	url(r'^main','forum.views.main' ),
	url(r'^forum/(\d+)/$','forum.views.forum'),
	url(r'^thread/(\d+)/$', 'forum.views.thread'),
	url(r'^post/(new_thread|reply)/(\d+)/$', 'views.post'),
	url(r"^reply/(\d+)/$", "views.reply"),
	url(r"^new_thread/(\d+)/$", "views.new_thread"),
    
)
'''