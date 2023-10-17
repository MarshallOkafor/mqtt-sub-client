# Using paho library
import paho.mqtt.client as mqtt

# Test connection variables
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "LoRa/marshall-weather-data"

def on_connect(client, userdata, flags, rc):
    """
    Call back function to connect to the public broker
    and subscribe to a topic.
    """

    print(f"Connect with result code {rc}")
    client.subscribe(TOPIC)

def on_subscribe(client, userdata, mid, granted_qos):
    """
    Call back function to indcate successful subscription
    to a topic.
    """

    print(f"Subscribed to {TOPIC}")

def on_message(client, userdata, msg):
    """
    Call back function to print received data.
    """

    print(f"Received data:\n '{msg.payload.decode()}' on topic '{msg.topic}'")

# Driver code
client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message 

client.connect(BROKER, PORT, 60)

# Keep listening for incoming data
client.loop_forever()