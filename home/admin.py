from django.contrib import admin
from home.models import Contact
from home.forms import ContactForm

# Register your models here.
admin.site.register(Contact)
