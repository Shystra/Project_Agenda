from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login (request):
    return render (request, 'accounts/login.html')

def logout (request):
    return render (request, 'accotuns/logout.html')



# ------------ AJUSTANDO CADASTRO -------------------
def cadastro (request):
    #messages.success(request, 'Deu certo!')
    if request.method != 'POST':  #SE FOR DIFERENTE DE POST
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get ('nome')
    sobrenome = request.POST.get ('sobrenome')
    email = request.POST.get ('email')
    usuario = request.POST.get ('usuario')
    senha = request.POST.get ('senha')
    senha2 = request.POST.get ('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha \
    or not senha2:
        messages.error (request, 'Por gentileza preencher os campos vazios.')
        return render (request, 'accounts/cadastro.html')
    
    # ----------- PARA VALIDAÇÃO E-MAIL ----------
    try:
        validate_email(email)
    except:
        messages.error (request, 'E-mail inválido')
        return render (request, 'accounts/cadastro.html')
    
    # -------- PARA VALIDAÇÃO SENHA & USUÁRIO --------
    if len(senha) <6:
        messages.error(request, 'Senha precisa ter 6 caractéres ou mais.')
        return render (request, 'accounts/cadastro.html')
    if senha != senha2:
        messages.error(request, 'Senha não conferem.')
        return render (request, 'accounts/cadastro.html')

    
    if len (usuario) <6:
        messages.error(request, 'Usuário precisa ter 6 caractéres ou mais.')
        return render(request, 'accounts/cadastro.html')
    

    # -------- AJUSTANDO USUARIO ADMIN ----------
    if User.objects.filter (username = usuario).exists():
        messages.error (request, 'Usuário já existente.')
        return render (request, 'accounts/cadastro.html')
    
    if User.objects.filter (email = email).exists ():
        messages.error (request, 'E-mail já existente.')
        return render (request, 'accounts/cadastro.html')
    


    # SE TUDO ISSO FOR OK!!! RETORNAR USUARIO REGISTRADO
    messages.success (request, 'Registrado com sucesso!')

    user = User.objects.create_user (username = usuario, email = email,
                                     password=senha, first_name=nome,
                                     last_name = sobrenome)
    user.save()
    return redirect ('login')
    # ------------ SE PASSOU AQUI DEU BOA PO -----------------


    print(request.POST)
    return render (request, 'accounts/cadastro.html')

def dashboard (request):
    return render (request, 'accounts/dashboard.html')

