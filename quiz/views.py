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

