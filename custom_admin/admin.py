from django.contrib import admin
from .models import *

class AdminMessage(admin.ModelAdmin):
    model=Message
    list_display=['name','date','read']

admin.site.register(Message,AdminMessage)