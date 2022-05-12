from core.models import Carro, Montadora

# OneToOne
carro = Carro.objects.get(pk=1)
carro

chassi = carro.chassi
chassi

# OneToMany

montadora = Montadora.objects.get(pk=1)
carros = montadora.carro_set.all()

carros

# ManyToMany
carro = Carro.objects.get(pk=1)
motoristas = carro.motoristas.all()
motoristas


# Pesquisa IN e DISTINCT
Carro.objects.filter(motoristas__in=motoristas).distinct()

"""
on_delete=CASCADE
on_delete=SET_DEFAULT, default='VALOR'
on_delete=SET(funcao_personalizada)


Função 
objects.get_or)create(nome='Padrão')[0] -- Busca um valor ou cria

Retorna uma tupla, sendo (Objeto, Criado_boolean)

Ex.
Montadora.objects.get_or)create(nome='Fiat')[0]

(Objeto Montadora, foi criado?)

por isso o [0] para pegar o objeto

"""