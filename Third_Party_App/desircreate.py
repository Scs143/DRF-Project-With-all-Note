import requests
import json

URL = "http://127.0.0.1:8000/drfcreate/"


data = {
    'teacher_name': 'Rahul New',
    'course_name': "Physics",
    'course_duration': 3,
    'seat': 20
}

json_data = json.dumps(data) # dumps convert python data into json data
r = requests.post(url=URL, data=json_data) # post request
data = r.json()
print(data)