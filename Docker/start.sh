#!/bin/sh

# Start the Mosquitto broker in the background
mosquitto -c /mosquitto/conf.d/default.conf &

# Wait until the broker is up and running by repeatedly trying to connect
while ! nc -z localhost 1883; do   
  echo "Waiting for Mosquitto broker to start..."
  sleep 1
done


# Start the publisher script
python3 /pub.py