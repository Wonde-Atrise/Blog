from django.contrib import admin

# Register your models here
from .models import Blogmodel,Message
admin.site.register(Blogmodel)
admin.site.register(Message)
