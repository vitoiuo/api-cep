from django.shortcuts import render, redirect
from api.models import Cep


# Create your views here.

def index(request):
    return render(request, 'consulta/index.html')


def consulta_por_cep(request):
    resposta_consulta = {}

    cep = request.GET.get('cep')

    if str(cep).isnumeric() and cep is not None:
        try:
            endereco = Cep.objects.get(cep=cep)

            formatted_cep = ''

            for i in cep:
                formatted_cep += i
                if len(formatted_cep) == 5:
                    formatted_cep += '-'

            if endereco.logradouro and endereco.complemento is not None:
                resposta_consulta = {
                    'cep': formatted_cep,
                    'logradouro': f'{endereco.logradouro} {endereco.complemento}',
                    'bairro': endereco.bairro,
                    'cidade': endereco.cidade.nome,
                    'estado': f'{endereco.cidade.estado.nome} ({endereco.cidade.estado.sigla})',
                }

            else:
                resposta_consulta = {
                    'cep': formatted_cep,
                    'logradouro': endereco.logradouro,
                    'complemento': endereco.complemento,
                    'bairro': endereco.bairro,
                    'cidade': endereco.cidade.nome,
                    'estado': f'{endereco.cidade.estado.nome} ({endereco.cidade.estado.sigla})',
                }

        except Cep.DoesNotExist:
            return redirect('consulta:consulta_por_cep')

    if not str(cep).isnumeric() and cep is not None:
        return redirect('consulta:consulta_por_cep')

    return render(request, 'consulta/consulta_por_cep.html', {'resposta_consulta': resposta_consulta})
