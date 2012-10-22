from django.forms import ModelForm
from django import forms
from forum import models

class ProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        exclude = ["posts", "user"]