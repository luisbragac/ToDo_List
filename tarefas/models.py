from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    opcoes_prioridade = [
        ('Alta', 'Alta'),
        ('Média', 'Média'),
        ('Baixa', 'Baixa'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    titulo = models.CharField(max_length=50)

    descricao = models.TextField(max_length=70, blank=True)

    data = models.DateField()

    concluida = models.BooleanField(default=False)

    prioridade = models.CharField(max_length=30, choices=opcoes_prioridade)

    def __str__(self):
        return self.titulo