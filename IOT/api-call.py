import requests
import paho.mqtt.client as mqtt

# Traccar API details
traccar_url = 'http://20.205.120.72:8082'
device_id = 1
username = 'admin@gmail.com'
password = 'Deployment123!'

# MQTT broker details
broker_url = '0.tcp.ap.ngrok.io'
broker_port = 13176
topic = 'device/1/location'

# send API request to get device location
response = requests.get(f'{traccar_url}/api/positions?deviceId={device_id}&maxResults=1', auth=(username, password))

if response.ok:
    # extract location data from response JSON
    location = response.json()[0]
    latitude = location['latitude']
    longitude = location['longitude']
    accuracy = location['accuracy']

    # send location data to MQTT broker
    client = mqtt.Client()
    client.connect(broker_url, broker_port)
    client.publish(topic, f'{{"latitude": {latitude}, "longitude": {longitude}, "accuracy": {accuracy}}}')
    client.disconnect()
else:
    print('Error retrieving location:', response.text)
