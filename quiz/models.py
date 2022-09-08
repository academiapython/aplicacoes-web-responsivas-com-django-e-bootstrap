from django.db import models

# Create your models here.
class Questao(models.Model):
    enunciado = models.TextField(max_length=255, null=False, blank=False, default="")
    imagem = models.ImageField(null=True, blank=True, default="")

    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    texto = models.TextField(max_length=255, null=False, blank=False, default="")
    isCorreta = models.BooleanField(default=False, null=True, blank=True)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

