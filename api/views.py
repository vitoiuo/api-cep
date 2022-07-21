from django.http import JsonResponse
from .models import Estado, Cidade, Cep


# Create your views here.

def api_consulta_cep(request, cep):
    endereco = Cep.objects.filter(cep=cep)

    if not endereco:
        resposta_consulta = {
            'cep': 'cep inválido'
        }

    if endereco:
        resposta_consulta = {
            'cep': endereco[0].cep,
            'logradouro': endereco[0].logradouro,
            'complemento': endereco[0].complemento,
            'bairro': endereco[0].bairro,
            'cidade_id': endereco[0].cidade_id,
            'cidade': {
                'id': endereco[0].cidade.id,
                'nome': endereco[0].cidade.nome,
            }

        }

    return JsonResponse(resposta_consulta)
