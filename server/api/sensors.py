# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

# project resources
from api.errors import forbidden

# external packages
import time
import copy

start_time = time.time() * 1000
# start_time = start_time_now.strftime("%D %H:%M:%S")

sensor_states ={}

sensor_states["Bed Occupied LHS"] = start_time
sensor_states["Bed Occupied RHS"] = start_time
sensor_states["Sofa Occupied LHS"] = start_time
sensor_states["Sofa Occupied RHS"] = start_time
sensor_states["Dining Chair 1"] = start_time
sensor_states["Dining Chair 2"] = start_time
sensor_states["Dining Chair 3"] = start_time
sensor_states["Dining Chair 4"] = start_time
sensor_states["Oven Door"] = start_time
sensor_states["Fridge Door"] = start_time
sensor_states["Kettle Pressure / Fullness"] = start_time
sensor_states["Toilet Occupied"] = start_time

class SensorsApi(Resource):
    def get(self) -> Response:
        data = request.get_json()

        now = time.time() * 1000

        sensor_states_copy = copy.deepcopy(sensor_states)
        for key, value in sensor_states_copy.items():
            print(now - value)
            if (now - value) < 30000:
                sensor_states_copy[key] = "OK"
            else:
                sensor_states_copy[key] = "OLD"

        return jsonify({'result': sensor_states_copy})

    def post(self) -> Response:
        data = request.get_data()

        data = data.decode("utf-8")
        sensor = str(data)

        now = time.time() * 1000
        # time = now.strftime("%D %H:%M:%S")

        sensor_states[sensor] = now

        output = "OK"

        print(sensor_states)

        return jsonify({'result': output})