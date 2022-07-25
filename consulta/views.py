from django.shortcuts import render


# Create your views here.

def consulta_por_cep(request, cep):
    context = {
        'tipo_de_consulta': 'cep'
    }
    return render(request, 'consulta/index.html', context)
