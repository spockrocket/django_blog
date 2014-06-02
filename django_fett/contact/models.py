from django.db import models
from django import forms
from django.forms.widgets import *

# a simple contact form
class ContactMe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 30, 'title': "name"}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'size': 30, 'title': "sender"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'size': 75, 'title': "sender"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 74, 'rows': 8}))
    send_to_myself = forms.BooleanField(required=False)
