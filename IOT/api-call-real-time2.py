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

while True:
    devices_response = requests.get(f"{traccar_url}/api/devices", headers=headers, auth=(username, password))
    if devices_response.ok:
        devices = devices_response.json()
        for device in devices:
            device_id = device["id"]
            location_response = requests.get(f"{traccar_url}/api/positions?deviceId={device_id}&maxResults=1", headers=headers, auth=(username, password))
            if location_response.ok:
                location = location_response.json()[0]
                latitude = location["latitude"]
                longitude = location["longitude"]
                accuracy = location["accuracy"]
                battery_level = location["attributes"]["batteryLevel"]
                distance = location["attributes"]["distance"]
                total_distance = location["attributes"]["totalDistance"]
                motion = location["attributes"]["motion"]

                # Publish the location data to MQTT broker
                message = {"device_id": device_id, "latitude": latitude, "longitude": longitude, "accuracy": accuracy, "battery_level": battery_level, "distance": distance, "total_distance": total_distance, "motion": motion}
                mqtt_topic = f"device/{device_id}/location"
                client.publish(mqtt_topic, json.dumps(message))
                print(f"Published location data for device {device_id}: {message}")
            else:
                print(f"Error fetching location data for device {device_id} from Traccar API")

    else:
        print("Error fetching devices from Traccar API")

    # Wait for 10 seconds before fetching the next location for each device
    time.sleep(10)

# Disconnect from MQTT broker
client.disconnect()