from django.db import models
from django import forms
# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class AppItem(models.Model):
    name = models.CharField(max_length=200)

class UserInput(forms.Form):
    attrs = {
        "type": "text",
        "id": "user-input",
        "name": "user-input",
        "placeholder": "Enter text here",
        "rows": "4",
        "cols": "10"
    }
    user_input = forms.CharField(widget=forms.Textarea(attrs=attrs))
