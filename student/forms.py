from django import forms
from .models import Department


class DeptForm(forms.ModelForm):
    class Meta:
        models = Department
        fields = "__all__"
