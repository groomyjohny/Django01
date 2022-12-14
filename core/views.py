import json

import django.conf
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from core.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from core.serializers import *
from rest_framework.parsers import JSONParser
from datetime import *

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class ChartsView(TemplateView):
    template_name = 'charts.html'

@csrf_exempt
def chartDataView(request):
    data = JSONParser().parse(request)
    dateRange = [ datetime.strptime(i, "%Y-%m-%dT%H:%M:%S.%fZ") for i in data['dateRange'] ]
    procName = data['procName']
    samplingPoints = int(data['samplingPoints'])

    dateDelta = dateRange[1] - dateRange[0]
    dateStep = dateDelta/samplingPoints

    ret = []
    for i in range(samplingPoints):
        rangeLow = dateRange[0]+dateStep*i
        rangeHigh = rangeLow+dateStep
        qs = ProcessRecord.objects.filter(
            imageName=procName,
            timestampBegin__gte=rangeLow,
            timestampEnd__lte=rangeHigh,
        )

        totalNs = 0
        for i in qs: totalNs += i.cpuTimeNs
        ret.append([ rangeLow, totalNs ])

    return JsonResponse(ret, safe=False)

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
    if request.method == "GET": #TODO: implement a limit there
        qs = ProcessRecord.objects.all()
        s = ProcessRecordSerializer(qs, many=True)
        return JsonResponse(s.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        s = ProcessRecordSerializer(data=data)
        if s.is_valid():
            s.save()
            return JsonResponse('', status=201, safe=False)
        return JsonResponse(s.errors, status=400)

def singleRecord(request, id):
    rec = get_object_or_404(ProcessRecord, id=id)
    s = ProcessRecordSerializer(rec)
    return JsonResponse(s.data, safe=False)

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

    s = ProcessRecordSerializer(qs, many=True)
    return JsonResponse(s.data, safe=False)