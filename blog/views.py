from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('id')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
