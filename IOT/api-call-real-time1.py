import requests
import json
import time
import paho.mqtt.client as mqtt

# Traccar API details
traccar_url = 'http://20.205.120.72:8082'
username = 'admin@gmail.com'
password = 'Deployment123!'
headers = {"Accept": "application/json"}

# MQTT broker details
mqtt_broker = "0.tcp.ap.ngrok.io"
mqtt_port = 13176
# MQTT client setup
client = mqtt.Client()

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Fetch list of devices from Traccar API
response = requests.get(f"{traccar_url}/api/devices", headers=headers, auth=(username, password))
if response.ok:
    devices = response.json()
    print(f"Fetched {len(devices)} devices from Traccar API")
    
    while True:
        for device in devices:
            device_id = device["id"]
            device_name = device["name"]
            mqtt_topic = f"device/{device_id}/location"

            response = requests.get(f"{traccar_url}/api/positions?deviceId={device_id}&maxResults=1", headers=headers, auth=(username, password))
            if response.ok:
                location = response.json()[0]
                latitude = location["latitude"]
                longitude = location["longitude"]
                device_time = location["deviceTime"]

                message = {"latitude": latitude, "longitude": longitude, "device_time": device_time}
                client.publish(mqtt_topic, json.dumps(message))
                print(f"Published location data for {device_name}: {message}")
            else:
                print(f"Error fetching location data for {device_name} from Traccar API")
        time.sleep(10)

else:    
    print("Error fetching device list from Traccar API")
client.disconnect()