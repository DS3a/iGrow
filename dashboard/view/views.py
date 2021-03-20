from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Value

# Create your views here.

prompt = "Hello World"

def home(request):  # is called when a get request is made to localhost
    return render(request, "index.html")

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
    print(request.body)
    print(Value.__str__(Value))
    return JsonResponse({"request": str(request)})


def send_vals(request):  # runs this when a get req is sent to atmosphere_regulation
    data = [{"stufsdafjhabegffhsgvrjbghjkf": "stuff 1"},
            {"modify sensor 1": "too low, increase the value 2"}]
    return JsonResponse(data, safe=False)
