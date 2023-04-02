from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post, Comentario


def home(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def blog(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def comentar(request, post_id):
    comentario = request.POST['comentario']
    perfil = User.objects.all().first().perfil
    post = Post.objects.get(pk=post_id)

    comentario = Comentario(texto=comentario, perfil=perfil, post=post)
    comentario.save()

    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)

def comentar_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comentarios = Comentario.objects.filter(post=post)
    return render(request, "social/modal_comentar.html", { 'post': post, 'comentarios':comentarios })