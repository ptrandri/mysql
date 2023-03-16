import paho.mqtt.publish as publish

broker_url = "0.tcp.ap.ngrok.io"
broker_port = 15840
topic = "device/DDX04"

# Message to publish
payload = "This is a test message."

# Publish message
publish.single(topic, payload, hostname=broker_url, port=broker_port)
