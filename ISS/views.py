from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

from ISS.components.getISSLocation import getISSLocation

# url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
url = "https://api.twitter.com/2/tweets/sample/stream"

# Create your views here.
def sendISSLocation(request):
    data = getISSLocation()
    json_str=json.dumps(data)
    return HttpResponse(json_str)

def directMessage(request):
    bearertoken=request.headers['Authorization']
    headers={'Authorization': '{}'.format(bearertoken)}
    print(headers)
    message = json.loads(request.body)['message']
    print(message)
    sendData = {
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": "kkkdddlll3"
                },
                "message_data": {
                    "text": message,
                }
            }
        }
    }
    params = {
        "screen_name": 'manattan_me',
        #"count": 1,
    }
    # res = requests.post(url,data=sendData, headers=headers)
    res = requests.get(url, headers=headers)
    print(res)
    tweets = res.json()
    print(tweets)
    return HttpResponse()