from django.shortcuts import render


# Create your views here.

def consulta(request):
    return render(request, 'consulta/index.html')
