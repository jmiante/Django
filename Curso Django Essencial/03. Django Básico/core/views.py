from django.shortcuts import render


def index(request):
    print(request.user)

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário Não Logado'
    else:
        teste = f'Bem vindo {request.user}'
        
    context = {
        'curso': 'Programação com Web com Django Frameword',
        'outro': 'Curso',
        'user': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
