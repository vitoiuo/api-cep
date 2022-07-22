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
            'estado': f'{endereco.cidade.estado.nome}, {endereco.cidade.estado.sigla}',
        }

    except Cep.DoesNotExist:
        resposta_consulta = {
            'cep': 'cep inválido',
        }

    return JsonResponse(resposta_consulta)
