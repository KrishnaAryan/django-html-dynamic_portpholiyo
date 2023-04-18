from django.shortcuts import render, redirect
from .models import *
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to success page or display success message
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})