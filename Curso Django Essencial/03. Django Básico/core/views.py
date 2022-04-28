from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação com Web com Django Frameword',
        'outro': 'Curso'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
