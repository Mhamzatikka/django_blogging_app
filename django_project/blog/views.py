from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
    'author': 'Talha',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'January 26, 2023'
    },
    {   
    'author': 'Talha',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'February 26, 2023'
    }
]

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)

def print_data(request):
    
    mymembers = Post.objects.all().values()
    context = {'mymembers': mymembers,}
    print(context)
    return render(request, 'blog/check.html', context)

def details(request, id):
    data = Post.objects.get(id=id)
    context = {'mymembers': data,}
    print("context is", context)
    return render(request, 'blog/check_by_id.html', context)

