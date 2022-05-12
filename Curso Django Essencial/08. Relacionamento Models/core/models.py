from django.contrib.auth import get_user_model
from django.db import models


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 Caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


class Carro(models.Model):
    """
    # OneToOneField
    Cada Carro só pode se relacionar com um Chassi
    Cada Chassi só pode se relacionar com um carro

    # ForeignKey (OneToMany)
    Cada carro tem uma montadora
    Cada montadora pode ter vários carros

    # ManyToMany
    Um carro pode ser dirigido por vários motorista
    e um motorista pode dirigir diversos carros
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 Caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.modelo} - {self.modelo}'

