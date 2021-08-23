from django import forms
from . models import List

class ListModelForm(forms.ModelForm):
    class Meta:
        model = List 
        fields = ("task",)   