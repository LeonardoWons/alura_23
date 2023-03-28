from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username=nome.lower(),
                password=senha.lower(),
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso")
                return redirect('index')
            else:
                messages.error(request, "Não foi possivel achar este usuario")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    sign = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["password1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Este nome ja existe")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome.lower(),
                email=email.lower(),
                password=senha.lower()
            )
            usuario.save()

            messages.success(request, f"{nome} criado com sucesso")

            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": sign})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout feito com sucesso")
    return redirect('login')
