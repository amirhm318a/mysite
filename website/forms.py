
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from website.models import Contact,Newsletter

from captcha.fields import CaptchaField




class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'