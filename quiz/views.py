from django.shortcuts import render
from django.contrib import messages
from quiz.models import Questao
from django.http.response import HttpResponse


# Create your views here.
def get_quiz(request):
    questao = Questao.objects.get(pk=3)
    context = {
        'questao': questao
    }
    return render(request, 'quiz/quiz.html', context)


def get_resposta(request):

    resposta = request.POST.get('resposta')

    if resposta == 'True':
        return HttpResponse("<p style='color:green'> Resposta Correta! </p>")
    elif resposta == 'False':
        return HttpResponse("<p style='color:red'> Resposta Incorreta. </p>")
    else:
        return HttpResponse("<p style='color:yellow'> Selecione uma alternativa. </p>")
