from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    firstpage_info = FirstPage.objects.get()
    about=About.objects.get()
    portfolio=Portfolio.objects.all()
    portfolio_image=PortfolioIimage.objects.all()
    your_skill=Skill.objects.all()
    experience= Experience.objects.all()
    blog=Blog.objects.all()
    your_contact=YourContactInfo.objects.get()
    resume=Resume.objects.get()
    context={
        'firstpage_info': firstpage_info,
        'about':about,
        'portfolio':portfolio,
        'portfolio_image':portfolio_image,
        'your_skill':your_skill,
        'experience':experience,
        'blog':blog,
        'your_contact':your_contact,
        'resume':resume
        }
    return render(request, 'index.html', context)

from .forms import ContactForm

from django.db import IntegrityError

import time
from django.shortcuts import redirect

def submitform(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.message = message
        
        try:
            contact.save()
            time.sleep(5)  # Delay the response by 5 seconds
            return HttpResponse("<h3> Your Form Has Been Received, I will contact You soon...😊 </h3><script>setTimeout(function(){window.location.href='/';},5000);</script>")
        except IntegrityError as e:
            return HttpResponse("<h3> Error Occurred While Saving Data: {}</h3>".format(str(e)))
            
    return render(request, 'index.html')
