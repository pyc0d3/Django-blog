from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def redirect_to_home(request):
    return redirect('blog-home')
