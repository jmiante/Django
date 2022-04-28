from django.shortcuts import render
from .models import Produto

def index(request):

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário Não Logado'
    else:
        teste = f'Bem vindo {request.user}'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação com Web com Django Frameword',
        'outro': 'Curso',
        'user': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(pk=pk)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)
