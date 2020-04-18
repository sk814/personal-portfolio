from django.shortcuts import render
from .models import Blog_Model

def all_blogs(request):
    blog_obj = Blog_Model.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog_obj': blog_obj})
