from django.shortcuts import render
from .models import Blog,Category
from django.core.paginator import Paginator



def BlogList(request):
    posts=Blog.objects.all().order_by('-created_time')
    paginator = Paginator(posts, 5)
    context={'posts':posts}
    return render(request,'blog.html',context)
