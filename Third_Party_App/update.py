import requests
import json

URL = "http://127.0.0.1:8000/drfcreate/"

data = {
    'id': 5,
    'teacher_name': 'Rahul Update',
    'course_name': "Math",
    'course_duration': 3,
    'seat': 20
}

json_data = json.dumps(data) # dumps convert python data into json data
r = requests.put(url=URL, data=json_data) # post request
data = r.json()
print(data)