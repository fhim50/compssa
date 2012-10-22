from django.core.urlresolvers import reverse
from settings import MEDIA_ROOT, MEDIA_URL
from forum.models import *
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forum import form

### image models
from PIL import Image as ProfileImage
from os.path import join


def main(request):
    """Main listing."""
    forums = Forum.objects.all()
    return render_to_response("forum/list.html", dict(forums=forums, user=request.user))
	
	
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items


def forum(request, pk):
    """Listing of threads in a forum."""
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    threads = mk_paginator(request, threads, 20)
    return render_to_response("forum/forum.html", add_csrf(request, threads=threads, pk=pk))
	
def thread(request, pk):
	""" listing of posts in thread """
	t= Thread.object.get(pk=pk)
	posts = Post.objects.filter(thread=pk).order_by("created")
	posts = mk_paginator(request,post, 15)
	title = Thread.objects.get(pk=pk).title
	return render_to_response("forum/thread.html", add_csrf(request, posts= posts ,pk=pk,title=t.title , media_url= MEDIA_URL, forum_pk=t.forum.pk ))
	
def post(request , ptype ,pk):
	""" Displays a post form """
	action = reverse("forum.views.%s" % ptype, args = [pk])
	if ptype == "new_thread":
		title = "Start New Topic"
		subject = ''
	elif ptype == "reply":
		title = "Reply"
		subject = "Re: " + Thread.objects.get(pk=pk).title
		
	return render_to_response("forum/post.html", add_crsf(request, subject= subject,))
def increment_post_counter(request):
	profile = request.user.profile_set.all()[0]
	profile.post += 1
	profile.save()
	
def new_thread(request, pk):
	""" create a new Thread """
	p = request.POST
	if p["subject"] and p["body"]:
		forum = Forum.objects.get(pk=pk)
		thread = Thread.objects.create(forum = forum, title=p["subject"],creator = request.user)
		Post.objects.create(thread=thread, title=p["subject"], body=p["body"], creator=request.user)
		increament_post_counter(request)
	return HttpResponseRedirect(reverse("forum.views.forum", args=[pk]))

def reply(request , pk):
	""" reply a thraed """
	if request.POST["body"]:
		thread = Thread.objects.get(pk=pk)
		post = Post.objects.create(thread=thread, title=request.POST["subject"],body = request.POST["body"],creator = request.user)
		increament_post_counter(request)
	return HttpResponseRedirect(reverse("forum.views.thread", args=[pk]) + "?page=last")
		
def profile(request, pk):
	pfile = UserProfile.objects.get(user = pk)
	img = None
	if request.method == "POST":
		profile = form.ProfileForm(request.POST, request.FILES, instance=profile)
		if pfile.is_valid():
			pfile.save()
			#resizing image and saving with same file name#
			
			imfn = join(MEDIA_ROOT, profile.picture.name)
			im = ProfileImage.open(imfn)
			im.thumbnail((160,160),ProfileImage.ANTIALIAS)
			im.save(imfn, "JPEG")
	else:
		pfile = form.ProfileForm(instance=profile)
		
	if profile.picture:
		img = "/media/" + profile.picture.name
	return render_to_response("forum/profile.html",  add_csrf(request, pfile=pfile, img=img)
	
	
	