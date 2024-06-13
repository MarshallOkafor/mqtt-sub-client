# Using paho library
import paho.mqtt.client as mqtt
import sys
import logging
from time import sleep

# Test connection variables
BROKER = "localhost"
PORT = 1883
TOPIC = "LoRa/NRG-lab-data"

def on_connect(client, userdata, flags, rc):
    """
    Call back function to connect to the public broker
    and subscribe to a topic.
    """

    print(f"Connect with result code {rc}")
    if rc == 0:
        client.subscribe(TOPIC, qos=0)
    else:
        print(f"Failed to connect, return code {rc}")

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

try:
    client.connect(BROKER, PORT, 60)
    print('Connected successfully to the Broker!')
except Exception as e:
    print(f'Unable to connect to Broker! Error: {e}')
    sys.exit(-1)

# Start the network loop
client.loop_start()

# Keep the main thread running to catch errors
while True:
    sleep(1)