from django.urls import path
from . import views

urlpatterns = [
    path('', views.contato, name='contato'),
    path('mensagem', views.processa_contato, name='mensagem'),
]