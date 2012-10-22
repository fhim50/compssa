from django.db import models
from django.contrib import admin
from string import join
from settings import MEDIA_ROOT
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	picture = models.ImageField("Profile Picture", upload_to="images/",blank=True, null=True)
	posts = models.IntegerField(default=0)
	user = models.ForeignKey(User, unique=True)
	def __unicode__(self):
		return unicode(self.user)
		
		
		
class Forum(models.Model):
	title = models.CharField(max_length = 60)
	def __unicode__(self):
		return self.title
		
	def num_posts(self):
		total_number_posts = sum([t.num_posts() for t in self.thread_set.all()])
		return total_number_posts
		
	def last_post(self):
		if self.thread_set.count():
			last = None
			for t in self.thread_set.all():
				l = t.last_post()
				if l:
					if not last or l.created > last:
						last = 1
					
					
			return last
		
class Thread(models.Model):
	title = models.CharField(max_length =60)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User, blank = True , null = True)
	forum = models.ForeignKey(Forum)
	
	
	def __unicode__(self):
		return unicode(self.creator) + " - " + self.title
	
	def num_posts(self):
		return self.post_set.count()
		
	def  num_replies(self):
		return self.post_set.count() -1
		
	def last_post(self):
		if self.post_set.count():
			return self.post_set.order_by("created")[0]
		
class Post(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User, blank=True, null=True)
	thread = models.ForeignKey(Thread)
	body = models.TextField(max_length=10000)
	
	def __uncode__(self):
		return u"%s - %s - %s" % (self.creator, self.thread, self.title)
		
	def short(self):
		return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
	short.allow_tags = True
	
	def profile_data(self):
		p = self.creator.userprofile_set.all()[0]
		return p.post, p.picture

def create_user_profile(sender, **kwargs):
	"""When creating a new user, make a profile for him."""
	u = kwargs["instance"]
	if not UserProfile.objects.filter(user=u):
		UserProfile(user=u).save()

post_save.connect(create_user_profile, sender=User)


### ADMIN SITE
class ForumAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "thread", "creator", "created"]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)

	