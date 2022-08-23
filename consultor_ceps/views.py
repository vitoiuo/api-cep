from django.shortcuts import render


# Create your views here.
def consultar_cep(request):
    return render(request, 'index.html')
