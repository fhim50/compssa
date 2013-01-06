from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib import admin

# models


class PublishedArticlesmanager(models.Manager):
	def get_query_set(self):
		return super(PublishedArticlesmanager, self).get_query_set().filter(is_published = True
				
)

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50, unique=True)
	text = models.TextField(help_text="Formatted using ReST", max_length = 200)
	author = models.ForeignKey(User)
	is_published = models.BooleanField(default=False, verbose_name="Publish?")
	created_on = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()
	published = PublishedArticlesmanager()
		
	def __unicode__(self):
		return self.title
				
	def save (self , *args , **kwargs ):
		if not self.slug:
			self.slug = slugify(self.title)
			super(Article , self).save(*args, **kwargs)
				
	@models.permalink
	def get_absolute_url(self):
		return ('wiki_article_details' , () , {'slug' : self.slug})
				
class Edit(models.Model):
	article = models.ForeignKey(Article)
	editor = models.ForeignKey(User)
	edited_on = models.DateTimeField(auto_now_add = True)
	summary = models.CharField(max_length = 100)
		
	class Meta:
		ordering = ['-edited_on']
				
	def __unicode__(self):
		return "%s - %s - %s" %(self.summary, self.editor, self.edited_on)
				
				
	@models.permalink
	def get_absolute_url(self):
		return ('wiki_edit_details' , self.id)
				
admin.site.register(Article)
admin.site.register(Edit)