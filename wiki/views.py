from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect ,render_to_response , get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list

# models modoles

from models import Article , Edit

#importin forms 

from forms import ArticleForm , EditForm

#add article view
@login_required
def add_article(request):
	form = ArticleForm(request.Post or None)
	if form.is_valid(): #  if something was typed in  the form do
		article = form.save(commit = False)
		article.author = request.user
		article.save()
		msg = " Article was saved successfully"
		message.sucess(request , msg , fail_silently = True)
		return redirect(article)
		
	return  render_to_response('wiki/article_form.html', dict (form = form ), context_instance = RequestContext(request))

	
@login_required
def edit_article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	form = ArticleForm(request.POST or None , instance = article)
	edit_form = EditForm(request.POST or None)
	if form.is_valid():
		article = form.save()
		if edit_form.is_valid():
			edit = edit_form.save(commit = False)
			edit.article = article
			edit.editor = request.user
			edit.save()
			msg = "Arcticle Updated Successfully"
			messages.success(request , msg , fail_silently = True)
			return redirect(article)
	return render_to_response('wiki/article_form.html',dict(form = form ,edit_form = edit_form , article = article) , context_instance = RequestContext(request))
	
	
def article_history(request , slug):
	article = get_object_or_404(Article , slug = slug)
	return object_list(request , queryset = Edit.ojects.filter(article__slug = slug),extra_context = {'article': article})
		