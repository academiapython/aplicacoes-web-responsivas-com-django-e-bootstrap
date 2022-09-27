from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_quiz, name='get_quiz'),
    path('quiz/resposta/', views.get_resposta, name='resposta')
]