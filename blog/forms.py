from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import comment


class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ['post','name','email','subject','message']