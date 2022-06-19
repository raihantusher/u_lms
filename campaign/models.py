from django.db import models
from email_list.models import EmailList, TemplateList
# Create your models here.
from mainapp.models import  Victim

class CampaignList(models.Model):
    name = models.CharField(max_length=160)
    list = models.ForeignKey(EmailList, on_delete=models.CASCADE)
    template = models.ForeignKey(TemplateList, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    launched_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    campaign = models.ForeignKey(CampaignList, related_name="logs", on_delete=models.CASCADE)
    email = models.ForeignKey(Victim, on_delete=models.CASCADE)
    is_opened = models.BooleanField(default=False)
    clicked = models.IntegerField(default=0)
