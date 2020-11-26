from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    data={
        'id': 8
    }
    json_str=json.dumps(data)
    print(request)
    print(HttpResponse(json_str,content_type="application/json, charset=utf-8"))
    return HttpResponse(json_str)