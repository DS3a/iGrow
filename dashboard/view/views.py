from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

prompt = "Hello World"


def home(request):  # is called when a get request is made to localhost
    global prompt
    #return HttpResponse(str(prompt))
    print(request.POST)
    return HttpResponse(str(prompt))
#    return render(request,"login.html")#,{"Name":name,'Class':clas,'School':school,'AdmissionNumber':adm,'Email':email,'user_id':userid,'passwd':'*****'})
    


def get_sensor_vals(request):  # runs this when a post req is sent to sensor_vals_input
    print(request.body)
    global prompt
    prompt = str(request.body)
    return JsonResponse({"request": str(request)})


def send_vals(request):  # runs this when a get req is sent to atmosphere_regulation
    data = [{"stufsdafjhabegffhsgvrjbghjkf": "stuff 1"},
            {"modify sensor 1": "too low, increase the value 2"}]
    return JsonResponse(data, safe=False)
