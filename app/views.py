from django.shortcuts import render

from app.models import Celular


def home(request):
    return render(request,'home.html')

def celulares(request):
    return render(request,'celulares.html')

def iphone(request):
    filtro = None
    if request.method == 'POST':
        filtro = Celular.objects.filter(marca__icontains='iphone')
    context = {
        "filtro": filtro
    }
    return render(request, 'iphone.html', context)

def pesquisar(request):
    pass

def listar_todos(request):
    celulares=Celular.objects.all()
    context={
        "celulares": celulares
    }
    return render(request, 'home.html', context)

def favoritos(request):
    pass
    return render(request,'favoritos.html')
