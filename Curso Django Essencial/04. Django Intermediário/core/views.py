from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            """
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Nome: {}, E-mail: {}, Assunto: {}'.format(nome, email, assunto))
            print('Mensagem: {}'.format(mensagem))
            """
            form.send_mail()
            messages.success(request, 'Enviado com Sucesso!!!')
        else:
            messages.error(request, 'Erro ao enviar E-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                """
                prod = form.save(commit=False)
                print(f'Nome: {prod.nome}')
                print(f'Estoque: {prod.estoque}')
                print(f'Preço: {prod.preco}')
                print(f'Imagem: {prod.imagem}')
                """
                messages.success(request, 'Produto Salvo com Sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')
