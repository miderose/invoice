# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.db.models import Q

from acquisti.models import Fornitore, Prodotto, Unita_misura


def get_lista_fornitori(request):
    chars = request.GET.get('term', '')
    if chars:
        to_return = Fornitore.objects.filter(ragione_sociale__icontains=chars)
    else:
        to_return = Fornitore.objects.all()
    
    to_return = list(to_return.values_list("ragione_sociale", flat=True))
    
    return HttpResponse(json.dumps(to_return), mimetype="application/json")


def get_lista_prodotti(request):
    chars = request.GET.get('term', '')
    if chars:
        to_return = Prodotto.objects.filter(nome__icontains=chars)
    else:
        to_return = Prodotto.objects.all()
    
    to_return = list(to_return.values_list("nome", flat=True))
    
    return HttpResponse(json.dumps(to_return), mimetype="application/json")


def get_lista_unita_misura(request):
    chars = request.GET.get('term', '')
    if chars:
        query = Q(nome__icontains=chars) | Q(abbreviazione__icontains=chars)
        to_return = Unita_misura.objects.filter(query)
    else:
        to_return = Unita_misura.objects.all()
    
    to_return = list(to_return.values_list("nome", flat=True))
    
    return HttpResponse(json.dumps(to_return), mimetype="application/json")



def get_ragione_sociale_by_id(request):
    return HttpResponse(Fornitore.objects.get(id=request.POST.get("id", 0)).ragione_sociale)


def get_nome_prodotto_by_id(request):
    return HttpResponse(Prodotto.objects.get(id=request.POST.get("id", 0)).nome)


def get_unita_di_misura_by_id(request):
    return HttpResponse(Unita_misura.objects.get(id=request.POST.get("id", 0)).abbreviazione)

