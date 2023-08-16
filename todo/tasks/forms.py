
from .models import *

from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'class':'input-group mb-3  form-control','placeholder':'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'