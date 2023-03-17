import paho.mqtt.client as mqtt
import pymongo
import json

mqtt_broker = "0.tcp.ap.ngrok.io"
mqtt_port = 10968
mongo_host = "192.168.100.201"
mongo_port = 27017
mongo_username = "mongoAdmin"
mongo_password = "KAb3747d"

# Connect to MongoDB
mongo_client = pymongo.MongoClient(f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}")
mongo_db = mongo_client["mqtt"]
mongo_collection = mongo_db["mqtt"]

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    mongo_collection.insert_one(data)
    print(f"Received data: {data}")

# MQTT client setup
client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port)
mqtt_topic = "device/+/location"
client.subscribe(mqtt_topic)
client.on_message = on_message
client.loop_forever()
