# Overview
This repository provides a simple MQTT subscriber client designed to connect to an MQTT broker. It supports connection to both a locally running MQTT broker and a Dockerized broker with a dummy publisher for testing purposes. This application uses the paho MQTT library.

# Setup
- Clone this repository
- Create a Python virtual environment:
```
python -m venv venv
```
- Activate the virtual environment:
```
# For Windows
venv\Scripts\activate

# For Unix or MacOS
source venv/bin/activate
```
- Install the required dependencies:
```
pip install -r requirements.txt
```
## Testing with Local Broker
Ensure you have an MQTT broker running on your localhost.
Run the application by using the Python command below to subscribe to the predefined topic:
```
python sub.py
```

**Note**: The application is configured to subscribe to a specific topic. To use a different topic, ensure that the topic is actively being published to by a publisher.


# Using Docker for a Complete Setup
If you do not have a local MQTT broker, you can use the provided Docker configuration which includes both a broker and a dummy publisher script that sends dummy data.
- Navigate to the Docker directory:
```
cd Docker
```
- Build the Docker image (optional - you can pull the image from Docker Hub). If you prefer to use the prebuilt and tested image, skip this step:
```
docker build -t mosquitto_with_publisher .
```
- Alternatively, pull the pre-built and tested image from Docker Hub, if you built the docker image using the Dockerfile, skip this step:
```
docker pull marshallokafor/mosquitto_with_publisher
```
- Run the container, ensuring to map the MQTT port to your host:
```
docker run -d -p 1883:1883 --name broker_server marshallokafor/mosquitto_with_publisher
```
- Run the sub.py script in the root directory to see the published data coming from the broker in the container:
```
python sub.py
```

# Additional Information
This setup is ideal for development and testing environments where you need a ready-to-use MQTT setup. The Docker container runs an MQTT broker and a script that publishes dummy data to a test topic, which the sub.py can subscribe to directly.

# License
See License