from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
