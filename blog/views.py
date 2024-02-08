from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post, Comentario
from django.shortcuts import redirect


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

def deletar_comentario(request, comentario_id):
    post = Comentario.objects.get(pk=comentario_id).post
    comentario = Comentario.objects.get(pk=comentario_id)
    comentario.delete()
    comentarios = Comentario.objects.filter(post=post)
    return render(request, "social/modal_comentar.html", {'post': post, 'comentarios': comentarios })

def editar_comentario(request, comentario_id):
    post = Comentario.objects.get(pk=comentario_id).post
    comentario = Comentario.objects.get(pk=comentario_id)

    context = {
        'comentario': comentario,
        'post': post
    }

    if request.method == "GET":
        return render(request, 'social/editar_comentario_modal.html', context)
    elif request.method == "POST":
        comentario.texto = request.POST['comentario']
        comentario.save()
        return redirect(request.path)
    return render(request, "social/editar_comentario_modal.html", context)
