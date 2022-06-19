from django import forms
from email_list.models import  TemplateList

class TemplateForm(forms.ModelForm):
    class Meta:
        model = TemplateList
        fields = "__all__"

