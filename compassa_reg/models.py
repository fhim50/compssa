from django.db import models
from django.contrib import admin

class Registration(models.Model):
   PROG = (
    ("BA", "BA")
    ("BSC","BSC")   
    )
    sur_name = models.CharField(max_length = 30)
    other_names = models.CharField(max_length = 30)
    program = models.CharField(max_length =5, choices = PROG, blank = True)
	phone_number = models.IntegerField(max_length = 10)
    hall = models.CharField(max_length = 30)
	hall_number = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 75, blank = True)
	
	
    

	
	
admin.site.register(School)
