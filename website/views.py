from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages
app_name='website'
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid:
           messages.success(request, 'Form submission successful')
           form.save()
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


def newslatter_view(request):
    if request.method == 'POST':
        form_news = NewsletterForm(request.POST)
        if form_news.is_valid():
            form_news.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit')

    form_news = NewsletterForm
    return(request,'website/contact.html',{'form_news':form_news})