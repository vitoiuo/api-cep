from django.http import JsonResponse
from .models import Cep


# Create your views here.

def api_consulta_cep(request, cep):
    endereco = Cep.objects.get(cep=cep)

    if not endereco:
        resposta_consulta = {
            'cep': 'cep inválido'
        }

    if endereco:
        resposta_consulta = {
            'cep': endereco.cep,
            'logradouro': endereco.logradouro,
            'complemento': endereco.complemento,
            'bairro': endereco.bairro,
            'cidade': {
                'id': endereco.cidade.id,
                'nome': endereco.cidade.nome,
                'estado': {
                    'id': endereco.cidade.estado.id,
                    'nome': endereco.cidade.estado.nome,
                    'sigla': endereco.cidade.estado.sigla,
                }
            }
        }

    return JsonResponse(resposta_consulta)
