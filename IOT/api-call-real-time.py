import requests
import json
import time
import paho.mqtt.client as mqtt

# Traccar API details
traccar_url = 'http://20.205.120.72:8082'
device_id = 1
username = 'admin@gmail.com'
password = 'Deployment123!'
headers = {"Accept": "application/json"}

# MQTT broker details
mqtt_broker = "0.tcp.ap.ngrok.io"
mqtt_port = 13176
mqtt_topic = "device/1/location"

# MQTT client setup
client = mqtt.Client()

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Keep publishing the latest device location to MQTT broker
while True:
    # Fetch latest device location from Traccar API
    response = requests.get(f"{traccar_url}/api/positions?deviceId={device_id}&maxResults=1", headers=headers, auth=(username, password))
    if response.ok:
        location = response.json()[0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        deviceTime = location['deviceTime']
        accuracy = location["accuracy"]

        # Publish the location data to MQTT broker
        message = {"latitude": latitude, "longitude": longitude, "DeviceTime": deviceTime, "accuracy": accuracy}
        client.publish(mqtt_topic, json.dumps(message))
        print(f"Published location data: {message}")
    else:
        print("Error fetching device location from Traccar API")

    # Wait for 10 seconds before fetching the next location
    time.sleep(10)

# Disconnect from MQTT broker
client.disconnect()
