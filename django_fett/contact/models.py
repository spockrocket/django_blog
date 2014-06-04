from django.db import models
from django import forms
from django.forms.widgets import *

# a simple contact form
class ContactMe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 30,'placeholder' : 'Your Name'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'size': 30, 'placeholder' : 'E-Mail Address'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'size': 75, 'placeholder' : 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 74, 'rows': 8, 'placeholder' : 'What\'s up?'}))
    send_to_myself = forms.BooleanField(required=False)
    #name.widget.attrs.update({'title': "Sender",})
    #sender.widget.attrs.update({'title': "E-Mail Address",})
    #subject.widget.attrs.update({ 'title': "Subject",})
    #message.widget.attrs.update({'title': 'Message',})
