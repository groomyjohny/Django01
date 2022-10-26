import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from core.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recordToJson(rec):
    return {
        'id': rec.id,
        'imagePath': rec.imagePath,
        'timestampBegin': rec.timestampBegin,
        'timestampEnd': rec.timestampEnd,
        'cpuTimeNs': rec.cpuTimeNs,
    }

def querySetToJson(qs):
    arr = [recordToJson(rec) for rec in qs]
    return arr
def allRecords(request):
    if request.method == "GET":
        qs = ProcessRecord.objects.all()
        return JsonResponse(querySetToJson(qs), safe=False)
    if request.method == "POST":
        return JsonResponse() #TODO: add DB insertion

def singleRecord(request, id):
    try:
        obj = ProcessRecord.objects.get(id=id)
        return JsonResponse(recordToJson(obj), safe=False)
    except ProcessRecord.DoesNotExist:
        return JsonResponse({'error': 'Record with specified ID was not found'}, status=404)

def filterRecords(request):
    # TODO: add input validation
    qs = ProcessRecord.objects.all()
    if 'idRange' in request.GET:
        args = request.GET['idRange'].split(',')
        qs = qs.filter(id__range=args)
    if 'timestampRange' in request.GET:
        args = request.GET['timestampRange'].split(',')
        qs = qs.filter(timestampBegin__lte=args[1], timestampEnd__gte=args[0])
    return JsonResponse(querySetToJson(qs), safe=False)