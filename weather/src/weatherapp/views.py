from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from config.settings import TEMPLATES

# Create your views here.

def index(request):
    #return HttpResponse("Weather for the address")
    #template = loader.get_template('weatherapp/index.html')
    return render(request,'first.html',{})

def contact(request):
    #return HttpResponse("Weather for the address")
    if request.method == "POST":
        cap_name = request.POST['name']
        cap_phone = request.POST['phone']
        print(cap_phone)
        return render(request, 'contact.html', {'cap_phone': cap_phone})
    else:
        return render(request,'contact.html',{})
