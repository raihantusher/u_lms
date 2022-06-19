from django.db import models

from email_list.models import EmailList
# Create your models here.

class Victim(models.Model):
    first_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    email = models.EmailField()
    list = models.ForeignKey(EmailList, related_name="emails", on_delete=models.CASCADE)

    def __str__(self):
        return self.email