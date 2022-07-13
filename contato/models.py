from django.db import models

CHOICES_ASSUNTO = [
    ('', 'Selecione um assunto'),
    ('descontos', 'Descontos'),
    ('consultoria', 'Consultoria'),
    ('freelance', 'Freelance'),
    ('elogios', 'Elogios'),
    ('reclamações', 'Reclamações'),
    ('outros', 'Outros'),
]

class Contato(models.Model):
    assunto = models.CharField(choices=CHOICES_ASSUNTO, default="", max_length=100)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)