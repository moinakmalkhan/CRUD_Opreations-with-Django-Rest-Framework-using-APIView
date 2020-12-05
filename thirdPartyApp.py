import requests
import json

URL = "http://127.0.0.1:8000/studentapifunctionbased/"
# URL = "http://127.0.0.1:8000/studentapiclassbased/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {"content-Type": "application/json"}
    jdata = json.dumps(data)
    req = requests.get(url=URL, data=jdata, headers=headers)
    data = req.json()
    print(data)


# getData()


def postData(data=None):
    if not data:
        data = {
            "name": "Ahmad",
            "roll": 4,
            "city": "Narowal"
        }
    headers = {"content-Type": "application/json"}
    json_data = json.dumps(data)
    req = requests.post(URL, data=json_data, headers=headers)
    res = req.json()
    print(res)


# postData()


def updateData(data=None):
    if not data:
        data = {
            "id": 4,
            "city": "Lahore"
        }
    headers = {"content-Type": "application/json"}
    json_data = json.dumps(data)
    req = requests.put(URL, data=json_data, headers=headers)
    res = req.json()
    print(res)


# updateData()


def deleteData(id):
    data = {'id': id}
    json_data = json.dumps(data)
    headers = {"content-Type": "application/json"}
    req = requests.delete(URL, data=json_data, headers=headers)
    res = req.json()
    print(res)


# deleteData(4)
