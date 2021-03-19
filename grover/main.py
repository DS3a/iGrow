import requests
import time
import numpy as np

time_to_sleep = 5

# structure of parameter {"name":{"lower_lim":ll, "upper_lim":ul, "unit":"unt", "rounding_factor":rf]}


class Grover:
    def __init__(self, params):
        self.payload = dict()
        self.params = params

    def get_values(self):
        for key in self.params.keys():
            val = np.random.uniform(self.params[key]["lower_lim"], self.params[key]["upper_lim"])
            val = round(val, self.params[key]["rounding_factor"])
            self.payload[key] = str(val) + " " + self.params[key]["unit"]
        return self.payload


tomato_ranges = {"Temperature": {"lower_lim": 10, "upper_lim": 25, "unit": "Centigrade", "rounding_factor": 2},
                 "Pressure": {"lower_lim": 0.9, "upper_lim": 1.15, "unit": "Bar", "rounding_factor": 4},
                 "Humidity": {"lower_lim": 50, "upper_lim": 70, "unit": "%", "rounding_factor": 2},
                 "pH": {"lower_lim": 5.5, "upper_lim": 6.8, "unit": " ", "rounding_factor": 1},
                 "Intensity": {"lower_lim": 1390, "upper_lim": 1410, "unit": "Lumen", "rounding_factor": 2},
                 }
grover_tomato = Grover(tomato_ranges)


while True:
    payload = grover_tomato.get_values()
    payload["time"] = time.time()
    resp = requests.post("http://127.0.0.1:8000/sensor_vals_input/", json=payload)
    print("sending request : ", payload)
    resp = requests.get("http://127.0.0.1:8000/atmosphere_regulation/")  # {""}
    print(resp.json())
    time.sleep(time_to_sleep)
