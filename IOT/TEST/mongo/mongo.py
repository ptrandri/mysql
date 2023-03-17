import paho.mqtt.client as mqtt
import pymongo
import json

# MongoDB details
mongo_url = "mongodb://mongoAdmin:KAb3747d@192.168.100.201:27017"
mongo_db = "mqtt"
mongo_collection = "mqtt"

mqtt_broker = "0.tcp.ap.ngrok.io"
mqtt_port = 10968

# Define callback function for when a message is received on a subscribed topic
def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    client = pymongo.MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db[mongo_collection]
    collection.insert_one(data)
    print(f"Data inserted into MongoDB: {data}")

# MQTT client setup
client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port)

# Subscribe to MQTT topic
mqtt_topic = "device/+/location"
client.subscribe(mqtt_topic)
client.on_message = on_message

# Start MQTT client loop
client.loop_forever()
