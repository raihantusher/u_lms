from django.db import models



class EmailList(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class TemplateList(models.Model):
    name = models.CharField(max_length=75)
    subject = models.CharField(max_length=200, default="New Subject")
    from_mail = models.CharField(max_length=200)
    template_body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name