from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . usuario_form import PerfilForm
from django.http import HttpResponse


def criar_conta(request):
    if request.method == 'POST':
        profile = PerfilForm(request.POST)
        if profile.is_valid():

            usr = User.objects.create_user(
                first_name=profile.cleaned_data['first_name'],
                last_name=profile.cleaned_data['last_name'],
                username=profile.cleaned_data['username'],
                email=profile.cleaned_data['email'],
                password=profile.cleaned_data['password']
            )

            usr.save()
            return redirect('login')

        else:
            return render(request, 'contas/criar_conta.html', {'form': profile})
    else:
        return render(request, 'contas/criar_conta.html', {'form': PerfilForm()})



def htmx_valida_username(request):
    usernameParam = request.POST.get('username')
    if len(usernameParam) < 5:
        return HttpResponse("<label style='color:red;'>Tamanho mínimo de 5 caracteres.</label>")
    elif User.objects.filter(username=usernameParam):
        return HttpResponse("<label style='color:red;'>Usuário indisponível</label>")
    else:
        return HttpResponse("<label style='color:green;'>Usuário disponível</label>")



def htmx_valida_senha(request):
    pwd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if pwd_confirm != password:
        return HttpResponse("<label style='color:red;'>As senhas não coincidem.</label>")
    else:
        return HttpResponse("")



def htmx_valida_email(request):
    email = request.POST.get('email')
    if User.objects.filter(email=email):
        return HttpResponse("<label style='color:red;'>Email já cadastrado.</label>")
    else:
        return HttpResponse("")
