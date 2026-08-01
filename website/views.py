from django.shortcuts import render
from .models import Prato

def index(request):
    pratos = Prato.objects.filter(ativo=True)
    #Pega apenas as categorias únicas cadastradas no banco de dados
    categorias = Prato.objects.filter(ativo=True).values_list('categoria', flat=True).distinct()
    
    context = {
        'pratos': pratos,
        'categorias': categorias,
    }
    return render(request, 'website/index.html', context)

# Adicionamos o alias 'home' apontando para a mesma função para evitar qualquer erro de rota
home = index