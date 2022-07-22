from django.shortcuts import render, redirect
import urllib.request
import json

def consultar_cep(request):
    if request.method=='POST':
        cep = request.POST.get('cep')

        a = 'http://127.0.0.1:8000/api/cep/' + cep
        with urllib.request.urlopen(a) as url:
            dict_cep = json.loads(url.read().decode())
            context = {
                'response':dict_cep
            }
        return render(request, 'consultor-cep/show-infos.html', context)
        
    else:
        return render(request, 'consultor-cep/consultar-cep.html')
# Create your views here.
