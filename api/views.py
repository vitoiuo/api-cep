from django.shortcuts import render
from django.http import JsonResponse
from . import models


# Create your views here.

def ola_mundo(request, cep):
    cep = 1 
    return JsonResponse(request, cep)
