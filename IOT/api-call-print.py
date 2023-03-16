import requests
import datetime
# replace with your Traccar server URL, username, and password
traccar_url = 'http://20.205.120.72:8082'
username = 'admin@gmail.com'
password = 'Deployment123!'
device_id = 1

# send API request to get device location with authentication
response = requests.get(f'{traccar_url}/api/positions?deviceId={device_id}&maxResults=1', auth=(username, password))

if response.ok:
    # extract location data from response JSON
    location = response.json()[0]
    latitude = location['latitude']
    longitude = location['longitude']
    deviceTime = location['deviceTime']
    accuracy = location['accuracy']

    dt = datetime.datetime.strptime(deviceTime, '%Y-%m-%dT%H:%M:%S.%f%z')
    formatted_deviceTime = dt.strftime('%Y-%m-%d %H:%M:%S')


    print(f'Latitude: {latitude}, Longitude: {longitude}, DeviceTime: {formatted_deviceTime}, Accuracy: {accuracy} meters')
else:
    print('Error retrieving location:', response.text)
