from django.http import JsonResponse
from .models import Cep
from django.db.models import Model


# Create your views here.

def api_consulta_cep(request, cep):
    try:
        endereco = Cep.objects.get(cep=cep)

        resposta_consulta = {
            'cep': endereco.cep,
            'logradouro': endereco.logradouro,
            'complemento': endereco.complemento,
            'bairro': endereco.bairro,
            'cidade': endereco.cidade.nome,
            'estado': endereco.cidade.estado.nome,
            'estado_sigla': endereco.cidade.estado.sigla,
        }

    except:
        resposta_consulta = {
            'cep': 'cep inválido'
        }

    return JsonResponse(resposta_consulta)
