from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Weather for the address")
    return render(request,'index.html',{})

