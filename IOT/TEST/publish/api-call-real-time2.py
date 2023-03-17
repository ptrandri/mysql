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
mqtt_port = 10968
client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port)

while True:
    devices_response = requests.get(f"{traccar_url}/api/devices", headers=headers, auth=(username, password))
    if devices_response.ok:
        devices = devices_response.json()
        for device in devices:
            # device_id = device["id"]
            device_id = 1
            location_response = requests.get(f"{traccar_url}/api/positions?deviceId={device_id}&maxResults=1", headers=headers, auth=(username, password))
            if location_response.ok:
                location = location_response.json()[0]
                latitude = format(location["latitude"], ".7f")
                longitude = format(location["longitude"], ".7f")
                accuracy = location["accuracy"]
                battery_level = location["attributes"]["batteryLevel"]
                distance = location["attributes"]["distance"]
                total_distance = location["attributes"]["totalDistance"]
                motion = location["attributes"]["motion"]
                heartRate = location["attributes"]["heartRate"]
                bloodOxygen = location["attributes"]["bloodOxygen"]
                serverTime = location["serverTime"]
                deviceTime = location["deviceTime"]


                message = {"device_id": device_id, "latitude": latitude, "longitude": longitude, "accuracy": accuracy, "battery_level": battery_level, "distance": distance, "total_distance": total_distance, "motion": motion, "heartRate": heartRate, "bloodOxygen":bloodOxygen, "serverTime": serverTime, "deviceTime": deviceTime }
                mqtt_topic = f"device/{device_id}/location"
                client.publish(mqtt_topic, json.dumps(message))
                print(f"Published location data for device {device_id}: {message}")
            else:
                print(f"Error fetching location data for device {device_id} from Traccar API")
    else:
        print("Error fetching devices from Traccar API")
    time.sleep(60)
client.disconnect()