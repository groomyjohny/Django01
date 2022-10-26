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
def allRecords(request):
    if request.method == "GET":
        qs = ProcessRecord.objects.all()
        arr = [recordToJson(rec) for rec in qs]
        return JsonResponse(arr, safe=False)
    if request.method == "POST":
        return JsonResponse()

def singleRecord(request, id):
    try:
        obj = ProcessRecord.objects.get(id=id)
        return JsonResponse(recordToJson(obj), safe=False)
    except ProcessRecord.DoesNotExist:
        return JsonResponse({'error': 'Record with specified ID was not found'}, status=404)

def filterRecords(request):
    return JsonResponse({},safe=False)