from channels.generic.websocket import WebsocketConsumer
from time import sleep
from .models import Value
import json

class WSConsumer(WebsocketConsumer):
    def connect(self):
        print("sending stuff on the websocket")
        value_obj = Value.objects.last()
        msg_dict = dict()
        msg_dict["Temperature"] = value_obj.Temperature
        msg_dict["Pressure"] = value_obj.Pressure
        msg_dict["Humidity"] = value_obj.Humidity
        msg_dict["pH"] = value_obj.pH
        msg_dict["Intensity"] = value_obj.Intensity
        print(msg_dict)
        self.accept()
        self.send(json.dumps(msg_dict))
        sleep(5)
