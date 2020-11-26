from django.shortcuts import render
from django.http import HttpResponse
import json

from ISS.components.getISSLocation import getISSLocation

# Create your views here.
def sendISSLocation(request):
    data = getISSLocation()
    json_str=json.dumps(data)
    print(HttpResponse(json_str,content_type="application/json, charset=utf-8"))
    return HttpResponse(json_str)