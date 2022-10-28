import json

import django.conf
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from core.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

def chartsView(request):
    return render(request, 'charts.html')

def querySetToJson(qs):
    arr = [rec.toDict() for rec in qs]
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
        arr = json.loads(request.body)
        for item in arr:
            m = ProcessRecord.fromDict(item)
            m.save()
        return JsonResponse() #TODO: add DB insertion

def singleRecord(request, id):
    rec = get_object_or_404(ProcessRecord, id=id);
    return JsonResponse(rec.toDict(), safe=False)

def filterRecords(request):
    # TODO: add input validation
    #TODO: add handling of multiple filters of same type (like imagePathContains + imagePathContains, etc). Note: make it accept a list of criteria
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
    if 'imageNameContains' in request.GET:
        qs = qs.filter(imageName__contains=request.GET['imageNameContains'])
    if 'imageNameExact' in request.GET:
        qs = qs.filter(imageName=request.GET['imageNameExact'])

    return JsonResponse(querySetToJson(qs), safe=False)