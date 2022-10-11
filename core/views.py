import json

import django.http
from django.shortcuts import render
import core.models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def allPersons(request):
    qs = core.models.Person.objects.all()
    arr = []

    for p in qs:
        arr.append({
            'id': p.id,
            'name': p.name,
            'phone': p.phone,
        })
    return django.http.JsonResponse({'results': arr})

def person(request, id):
    p = core.models.Person.objects.get(id=id)
    ret = {
        'id': p.id,
        'name': p.name,
        'phone': p.phone,
    }
    return django.http.JsonResponse(ret)