from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blogs/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
	detailblog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/detail.html', {'blog':detailblog})

def bio(request):
	return render(request, 'blogs/bio.html')

def video(request):
	return render(request, 'blogs/videos.html')
