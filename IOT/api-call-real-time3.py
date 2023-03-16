import requests
import json
import time

# Traccar API details
traccar_url = 'http://20.205.120.72:8082'
username = 'admin@gmail.com'
password = 'Deployment123!'
headers = {"Accept": "application/json"}

# Keep fetching and printing the latest location data for all devices
while True:
    # Fetch latest location data for all devices from Traccar API
    response = requests.get(f"{traccar_url}/api/positions", headers=headers, auth=(username, password))
    if response.ok:
        positions = response.json()
        for position in positions:
            device_id = position["deviceId"]
            latitude = position["latitude"]
            longitude = position["longitude"]
            accuracy = position["accuracy"]
            timestamp = position["serverTime"]

            # Construct a JSON message and print it to the console
            message = {
                "deviceId": device_id,
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": accuracy,
                "timestamp": timestamp
            }
            print(json.dumps(message))
    else:
        print("Error fetching device locations from Traccar API")

    # Wait for 10 seconds before fetching the next location data
    time.sleep(10)
