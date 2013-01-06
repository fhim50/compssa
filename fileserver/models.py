from django.db import models
from django.contrib import admin
import os
import mimetypes
#from os.path import join
class Fileserver(models.Model):
	name = models.CharField(max_length = 64)
	path = models.CharField(max_length = 220)
	
	def __unicode__(self):
		return self.name
		
	def get_absolute_url(self):
		return '/files/%s/' % self.name
		
	def isdir(self, path):
		#os.path.dirname(os.path.realpath(__file__))
		#os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates'),
		p = os.path.realpath(os.path.join(self.path, path))
		if not p.startswith(self.path): 
			raise ValueError(path)
		return os.path.isdir(p)
			
	def files(self, path = ''):
		p = os.path.realpath(os.path.join(self.path, path))
		if not p.startswith(self.path):
			raise ValueError(path)
		
		l = os.listdir(p)
		if path:
			l.insert(0, '..')
			#pathtuple = (f, os.path.isdir(os.path.join(p, f))
			#type = (mimetypes.guess_type(f)[0] or 'application/octetstream')
			return [(f, os.path.isdir(os.path.join(p, f)) , mimetypes.guess_type(f)[0] or 'application/octetstream') for f  in l ]

	
	def file(self, path):
		p = os.path.realpath(os.path.join(self.path, path))
		if not p.statswith(self.path):
			(type,encoding) = mimetypes.guess_type(p)
			return (p, type or 'application/octetstream')
		else:
			raise ValueError(path)
			
class FileserverAdmin(admin.ModelAdmin):
	list_display = ('name', 'path',)
	search_fields = ('name', 'path',)
	ordering =['name']
		
	
	
admin.site.register(Fileserver, FileserverAdmin)