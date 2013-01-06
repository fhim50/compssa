from fileserver.models import Fileserver
from django.http import HttpResponseRedirect, HttpResponse ,Http404
from django.template import Context, loader
import os
#from django.http import Http404


def index(request):
	fslist = Fileserver.objects.all().order_by('name')
	t = loader.get_template('fileserver/index.html')
	c = Context(request, {'fslist':'fslist'})
	return HttpResponse(t.render(c))
	

	
def directory(request, fileserver_name, path):
	try:
		fs = Fileserver.objects.get(name__exact = fileserver_name)
		if fs.isdir(path):
			files = fs.files(path)
			template = loader.get_template('fileserver/directory.html')
			c = Context({'dlist':[f for (f ,d ,t) in files if d],'flist':[{'name':f , 'type':t} for (f ,d ,t) in files if not d],'path':path , 'fs':fs,})
			return HttpResponse(template.render(c))
		else:
			(f , mimetype) = fs.file(path)
			return HttpResponse(open(f).read(), mimetype=mimetype)
	except ValueError:
		raise Http404
	except Fileserver.DoesNotExist:
		raise Http404
		
	except IOError:
		raise Http404
	
	