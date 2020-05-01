from django.shortcuts import render,redirect
from .form import Blog
from .models import Blog_Model


def all_blogs(request):
    if request.method == 'GET':
        blog_obj = Blog_Model.objects.all().order_by('-id')
        return render(request, 'blog/all_blogs.html', {'form': Blog(),'blog_obj':blog_obj})
    else:
        try:
            form = Blog(request.POST)
            newurl = form.save(commit=False)
            newurl.save()
            return redirect(request.path_info)
        except ValueError:
            return render(request, 'blog/all_blogs.html',  {'form': Blog(),'error':'Bad data passed in. Please try again'})

