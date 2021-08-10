# RALT Custom Sensor Dashboard 

This repository contains the Docker dependencies for the RALT Custom Sensor Dashboard, which provides status information and test capability for the [RALT Custom Sensors](https://github.com/care-group/RALT-Custom-Sensors).

## Usage

The server and client can be run as standalone apps outside of Docker.

### Server

The server application can be run from the ```server``` directory with: ```python3 app.py``` and will be accessible on port 5000.

To add a sensor to the system, you must add an entry to the ```sensor_states``` dictionary in ```server/api/sensors.py```, as below:
```
sensor_states["Bed Occupied LHS"] = start_time # you must set initial state to this variable
```

Your sensor node (e.g. ESP8266) must then send a HTTP POST request to the server at the update endpoint ```[server_ip:5000/update]``` every few seconds (e.g. 5 seconds). The content of the message should be plain text matching the name of the sensor, e.g. ```Bed Occupied LHS```; there should be no other content sent to the server.

If the server does not hear from a sensor within 30 seconds of the previous contact, it will mark that sensor as offline.

### Client

The contents of the ```client``` directory contents can be uploaded to a web server and accessed via a web browser.