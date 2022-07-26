from django.http import JsonResponse, Http404
from .models import Cep


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
            'sigla': endereco.cidade.estado.sigla,
        }

        return JsonResponse(resposta_consulta, status=200)

    except Cep.DoesNotExist:
        resposta_consulta = {
            'cep': 'inválido',
        }

        return JsonResponse(resposta_consulta, status=404)
