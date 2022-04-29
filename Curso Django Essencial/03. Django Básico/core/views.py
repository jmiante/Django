from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

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
    #prod = Produto.objects.get(pk=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf-8', status=404)


def error500(request):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf-8', status=500)
