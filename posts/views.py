from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'posts/index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    # redirect('app_name:name')
    return redirect('posts:detail', id=post.id)