from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
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

def initFirebase():
    cred = credentials.Certificate("/Users/takanori/manattan/tweet-from-space-firebase-adminsdk-1jnjg-7f64d5bb72.json")
    firebase_admin.initialize_app(cred)

def directMessage(request):
    initFirebase()
    bearertoken=request.headers['Authorization']
    token = bearertoken.split(" ")[1]
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']
    user = auth.get_user(uid)
    print(user)
    # message = json.loads(request.body)['message']
    # print(message)
    # sendData = {
    #     "event": {
    #         "type": "message_create",
    #         "message_create": {
    #             "target": {
    #                 "recipient_id": "kkkdddlll3"
    #             },
    #             "message_data": {
    #                 "text": message,
    #             }
    #         }
    #     }
    # }
    # params = {
    #     "screen_name": 'manattan_me',
    #     #"count": 1,
    # }
    # # res = requests.post(url,data=sendData, headers=headers)
    # res = requests.get(url, headers=headers)
    # print(res)
    # tweets = res.json()
    # print(tweets)
    return HttpResponse(user)