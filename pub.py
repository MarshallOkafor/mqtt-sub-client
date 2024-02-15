"""
Test MQTT publisher node.

"""

# Required package
import paho.mqtt.client as mqtt
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG)
import sys
import json
 
BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'LoRa/NRG-lab-data'

# Pseudo data
data = {
    'deviceID': 'ESP_32_500',
    'location': [23, 78],
    'temp': '25.87C',
    'hum':'56%',
    'pres': '950.450hPa',
    'gas': '70KOhms'
}

# Driver code
if __name__ == '__main__':
    
    pub_client = mqtt.Client()
    if pub_client.connect(BROKER, PORT, 60) != 0:
        print('Unable to connect to Broker!')
        sys.exit(-1)
    else:
        print('Connected successfully to the Broker!')
    # Publish Pseudo data
    i = 0
    while (i < 3):
        pub_client.publish(TOPIC, json.dumps(data), 0)
        print('Data %d published successfully!' % i)
        i += 1
        sleep(2)
    # Disconnect from the broker
    pub_client.disconnect()