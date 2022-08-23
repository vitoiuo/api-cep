import json
from textwrap import indent

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Cep

# Create your views here.

def api_cep(request, cep):
    try:
        data = Cep.objects.select_related('cidade').values(
            'logradouro',
            'bairro',
            'complemento',
            'cidade__nome',
            'cidade__estado__nome',
            'cidade__estado__sigla'
            ).get(cep=cep)

        consulta = {
            'logradouro':data['logradouro'],
            'bairro':data['bairro'],
            'complemento':data['complemento'],
            'cidade':data['cidade__nome'],
            'estado':data['cidade__estado__nome'],
            'sigla':data['cidade__estado__sigla'],
        }
    except ObjectDoesNotExist:
        consulta = {
            'mensagem':'Cep inexistente'
        }
        
    return HttpResponse(json.dumps(consulta, ensure_ascii=False, indent=2), content_type="application/json")
