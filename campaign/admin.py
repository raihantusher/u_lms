from django.contrib import admin

# Register your models here.
from .models import CampaignList, Log

admin.site.register(CampaignList)
admin.site.register(Log)