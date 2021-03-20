from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Value
import json

# Create your views here.

prompt = "Hello World"

def home(request):  # is called when a get request is made to localhost
    return render(request, "Home.html")

def view_sensor_vals(request):  # is called when a get request is made to localhost
    global prompt
    #return HttpResponse(str(prompt))
    print(request.POST)
    all_values = Value.objects.all
    print("alll", all_values)
    return render(request, "sensor_vals.html", {"all":all_values})
#    return HttpResponse(str(prompt))



def get_sensor_vals(request):  # runs this when a post req is sent to sensor_vals_input
    global prompt
    prompt = str(request.body)
    req = json.loads(request.body)
    value_obj = Value.objects.last()
    value_obj.Temperature = req["Temperature"]
    value_obj.Pressure = req["Pressure"]
    value_obj.Humidity = req["Humidity"]
    value_obj.pH = req["pH"]
    value_obj.Intensity = req["Intensity"]
    value_obj.save()
    return JsonResponse({"request": str(request)})


def send_vals(request):  # runs this when a get req is sent to atmosphere_regulation
    data = [{"Humidity": "+2%"},
            {"pH": "-0.1"},
            {"Temperature": "+0"}]
    return JsonResponse(data, safe=False)
