from django.db import models
from django.contrib import admin

class Registration(models.Model):
    """
	HALLS = legon hall , Mensah Sarbah hall ,Akuafo hall, Common Wealth Hall ,Volta Hall
	Jean Nelson akah Hall ,Elizabeth frances sey, alexader Kwarpong, hilla limman,
	Africa Union Hall, evandy Hostels, Bani Hostels, TF hostel, Jubilee Hall....
	"""
	


    PROG = (("BA", "BA"),("Bsc","Bsc"), )
    LEVEL =(('L100','L100'),('L200','L200'),('L300','L300'),('L400','L400'),)
    ID = models.IntegerField(max_length = 8, primary_key = True)
    sur_name = models.CharField("Surname",help_text="Please Enter Your Surname",max_length = 30)
    other_names = models.CharField("Other Names",help_text="Please Enter Your Other Names",max_length = 30)
    programe = models.CharField(max_length =5, choices = PROG, blank = True)
    level = models.CharField(max_length =5, choices = LEVEL)
    phone_number = models.IntegerField(max_length = 10)
    hall = models.CharField(max_length = 30, blank = True,help_text="Optional")
    room_number = models.CharField(max_length = 30, blank = True,help_text="Optional")
    email = models.EmailField(max_length = 75, blank = True,help_text="Optional")
    #courses = models.CharField("Course(s)",max_length = 30, blank = True)
    remarks = models.TextField("Remarks",help_text="For Personnel Only",max_length = 300 , blank = True)
    def __unicode__(self):
       return (self.sur_name)

    class Meta:
       db_table = 'registration'
	
	
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('ID','sur_name','other_names','programe','phone_number','hall','room_number','email')
    search_fields = ('sur_name','other_names','programe','hall')
    list_filter = ('programe','level',)

	
	
admin.site.register(Registration,RegistrationAdmin)
