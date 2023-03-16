import requests
import json
import time

web_url = 'http://20.205.120.72:8082'
payload = 'api/positions?deviceId'
device = 1
username = 'admin@gmail.com'
password = 'Deployment123!'
headers = {"Accept": "application/json"}

response = requests.get(f"{web_url}/{payload}={device}", headers=headers, auth=(username, password))
if response.ok:
        positions = response.json()
        for dataload in positions:
            id = dataload["deviceId"]
            attributesindex = dataload["attributes"]["index"]
            message = {
                "Id": id, 
                "index": attributesindex
            }
            print(json.dumps(message))
else:
    print("Error fetching data from API")