import json

import django.conf
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from core.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recordToJson(rec):
    return {
        'id': rec.id,
        'imageName': rec.getImageName(),
        'imagePath': rec.imagePath,
        'osPid': rec.osPid,
        'osParentPid': rec.osParentPid,
        'timestampBegin': rec.timestampBegin,
        'timestampEnd': rec.timestampEnd,
        'cpuTimeNs': rec.cpuTimeNs,
    }

def jsonToRecord(js):
    rec = json.loads(js)
    return {
        'id': rec.id,
        'imageName': rec.getImageName(),
        'imagePath': rec.imagePath,
        'osPid': rec.osPid,
        'osParentPid': rec.osParentPid,
        'timestampBegin': rec.timestampBegin,
        'timestampEnd': rec.timestampEnd,
        'cpuTimeNs': rec.cpuTimeNs,
    }

def querySetToJson(qs):
    arr = [recordToJson(rec) for rec in qs]
    return arr

#view for records/
#GET: get all available records
#POST: expects an array of JSON records and inserts them to DB
if django.conf.settings.DEBUG:
    @csrf_exempt
    def allRecords(request):
        return allRecordsInner(request)
else:
    def allRecords(request):
        return allRecordsInner(request)

def allRecordsInner(request):
    if request.method == "GET":
        qs = ProcessRecord.objects.all()
        return JsonResponse(querySetToJson(qs), safe=False)
    if request.method == "POST":
        #arr = json.loads()
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
    if 'imagePathContains' in request.GET:
        qs = qs.filter(imagePath__contains=request.GET['imagePathContains'])
    if 'imagePathExact' in request.GET:
        qs = qs.filter(imagePath=request.GET['imagePathExact'])

    return JsonResponse(querySetToJson(qs), safe=False)