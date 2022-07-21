from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def ola_mundo(request):
    return HttpResponse('ola mundo', content_type='text/plain')
