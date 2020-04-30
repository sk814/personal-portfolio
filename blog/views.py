from django.shortcuts import render
from .form import Blog
from .models import Blog_Model

def all_blogs(request):


    if request.method == 'GET':
        blog_obj = Blog_Model.objects.all()
        return render(request, 'blog/all_blogs.html', {'blog_obj': blog_obj})
    else:
        try:
            form=Blog(request.POST)
            form.save(commit=True)
        except ValueError:
            return render(request, 'blog/all_blogs.html',  {'form': Blog(),'error':'Bad data passed in. Please try again'})





