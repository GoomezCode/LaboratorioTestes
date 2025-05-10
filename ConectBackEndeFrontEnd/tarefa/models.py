from django.db import models

# Create your models here.
class tarefaModel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
