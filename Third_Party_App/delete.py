import requests
import json

URL = "http://127.0.0.1:8000/drfcreate/"

data = {
    'id': 5,
}

json_data = json.dumps(data) # dumps convert python data into json data
r = requests.delete(url=URL, data=json_data) # post request
data = r.json()
print(data)