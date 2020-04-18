from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

def media(request):
    projects=Projects.objects.all()
    return render(request,'portfolio/homepage.html',{'projects':projects})

