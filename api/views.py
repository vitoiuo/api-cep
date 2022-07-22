from django.shortcuts import render
from django.http import JsonResponse
from .models import Cep
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def api_cep(request, cep):
    try:
        data = Cep.objects.values('logradouro','bairro','complemento','cidade__nome','cidade__estado__nome').get(cep=cep)
        consulta = {
            'logradouro':data['logradouro'],
            'bairro':data['bairro'],
            'complemento':data['complemento'],
            'cidade':data['cidade__nome'],
            'estado':data['cidade__estado__nome'],
        }
    except ObjectDoesNotExist:
        consulta = {
            'mensagem':'Cep inexistente'
        }
    return JsonResponse(consulta)
