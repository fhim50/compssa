from django import forms
from models import *

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude =['author', 'slug'] # excluded author and slug because they will be auto filled
		
class EditForm(forms.ModelForm):
	class Meta:
		model = Edit
		fields = ['summary'] # including summary as the only fiels because article , editor and 
#				edited_on will be auto filled
		