import json

from django.http import JsonResponse, HttpResponse
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
    return JsonResponse({'results': arr})

def recordToJson(rec):
    return {
        'id': rec.id,
        'imagePath': rec.imagePath,
        'timestampBegin': rec.timestampBegin,
        'timestampEnd': rec.timestampEnd,
        'cpuTimeNs': rec.cpuTimeNs,
    }
def allRecords(request):
    if request.method == "GET":
        qs = core.models.ProcessRecord.objects.all()
        arr = [recordToJson(rec) for rec in qs]
        return JsonResponse(arr, safe=False)
    if request.method == "POST":
        return JsonResponse()

def singleRecord(request, id):
    ret = core.models.ProcessRecord.objects.filter(id=id)
    if len(ret) == 1: return JsonResponse(recordToJson(ret[0]), safe=False)
    else: return JsonResponse({}, status=404)

def person(request, id):
    p = core.models.Person.objects.get(id=id)
    ret = {
        'id': p.id,
        'name': p.name,
        'phone': p.phone,
    }
    return django.http.JsonResponse({ret})