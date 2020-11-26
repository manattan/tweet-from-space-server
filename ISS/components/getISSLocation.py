import requests
import json

def getISSLocation():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    locations = json.loads(res.text)['iss_position']
    return locations
