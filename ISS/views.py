from django.shortcuts import render
from django.http import HttpResponse
import json

from ISS.components.getISSLocation import getISSLocation

# Create your views here.
def sendISSLocation(request):
    data = getISSLocation()
    json_str=json.dumps(data)
    return HttpResponse(json_str)

def directMessage(request):
    token=request.headers['Authorization']
    headers={'Authorization': 'Bearer {}'.format(token)}
    data = json.loads(request.body)
    message = data['message']
    return HttpResponse()