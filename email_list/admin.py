from django.contrib import admin

# Register your models here.
from .models import EmailList, TemplateList

admin.site.register(EmailList)
admin.site.register(TemplateList)