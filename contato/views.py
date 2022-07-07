from django.shortcuts import render

def contato(request):
    return render(request, 'contato/contato.html')
