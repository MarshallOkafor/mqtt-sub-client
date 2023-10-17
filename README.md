# Overview
This is a simple MQTT subscriber client to the **Eclipse** public broker. This application uses the **paho** MQTT library.

# Setup
- Clone this repository
- Create a Python ```venv``` using the command below
```
python -m venv venv
```
- Install the paho library in the virtual environment using the ```pip``` command below
```
pip install -r requirements.txt
```

# Run the application
Run the application by using the Python command below. 
```
python sub.py
```

Note: The application is already programmed to subscribe to a topic for testing purposes. To use a different topic, you have to make sure that the topic is published to the broker by a publisher.