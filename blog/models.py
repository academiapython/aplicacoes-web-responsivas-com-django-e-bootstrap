from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now())
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
