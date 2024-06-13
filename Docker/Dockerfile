# Use the official Eclipse Mosquitto image
FROM eclipse-mosquitto:latest

# Install Python and pip (Alpine pachage manager)
RUN apk update && apk add --no-cache python3 py3-pip

# Copy the publisher script to the container
COPY pub.py /pub.py

# Install the paho-mqtt library
RUN pip3 install paho-mqtt==1.6.1

# Copy the mosquitto configuration file to the container
COPY default.conf /mosquitto/conf.d/default.conf

# Copy the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose the Mosquitto broker port
EXPOSE 1883

# Start the Mosquitto broker and the publisher script
CMD ["/start.sh"]