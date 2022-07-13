from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
import re
from exemplos.form_exemplo import FormExemplo


def get_bootstrap(request):
    return render(request, 'exemplos/16_forms_parte_i.html')

# Executa as seguintes validações:
'''
    1. ter tamanho mínimo 6 e no máximo 15 caracteres.
    2. Deves ter somente letras e numero e caractere especial(!#@$%&)
    3. Deve ter no mínimo uma letra maiúscula e minúscula.
    4. Deve ter no mínimo um numero.
    5. Deve ter no mínimo caractere especial(!#@$%&)
'''
def validou_senha(senha):
    regex = '^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{6,15}$'
    if (re.search(regex, senha)):
        return True
    else:
        return False


# Faz validação do email utilizando regex
def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        return True
    else:
        return False

# Caso email e senha tenha passado pela validação, retorna True
def validou_form(email, senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False


# Esta view é responsável por processar as requisições.
def processa_formulario_v1(request):

    email = request.POST.get("email")
    senha = request.POST.get("senha")

    # Atributos utilizados para indicar se os campos passaram ou não pela validação.
    email_st = 'is-valid'
    senha_st = 'is-valid'

    # se ambos passaram pela validação, redireciona para a página inicial
    if validou_form(email, senha):
        return HttpResponseRedirect("/")
    else:
        # caso não tenha passado pela validação, identifica qual campo apresenta erro.
        if not validou_email(email):
            email_st = 'is-invalid'
        if not validou_senha(senha):
            senha_st = 'is-invalid'

        # populando objeto de contexto para renderização de informações no template
        context = {
            "email": email,
            "senha": senha,
            "email_st": email_st,
            "senha_st": senha_st
        }

        return render(request, 'exemplos/16_forms_parte_i.html', context)


# esta view faz validações com base na classe FormExemplo.
def processa_formulario_v2(request):
    form = FormExemplo()

    if request.method == "POST":
        form = FormExemplo(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['senha']
            msg = form.cleaned_data['mensagem']
            return HttpResponse("Formulário validado com sucesso. {} - {} - {}".format(email, pwd, msg))
        else:
            print("Deu ruim!!!!")
    return render(request, 'exemplos/17_forms_parte_ii.html', {'form': form})


