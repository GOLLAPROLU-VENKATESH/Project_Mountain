from django.contrib import admin
from .models.contactus import ContactUs
from .models.contactusc import ContactUsc
# Register your models here.

class AdminContactUs(admin.ModelAdmin):
    list_display = ['last_name','email','phone_number']

admin.site.register(ContactUs,AdminContactUs)
admin.site.register(ContactUsc)