from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from config.settings import TEMPLATES
from django.core.mail import send_mail

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
        cap_email = request.POST['email']
        cap_subject = request.POST['subject']
        cap_message = request.POST['message']
        
        # send an email
        
        send_mail(
            'from '+ cap_name +' : ' + cap_subject, # subject
            cap_message , # message
            cap_email, # from email
            ['golmal1965@gmail.com'], # to email
        )

        return render(request, 'contact.html', {'cap_phone': cap_phone})
    else:
        return render(request,'contact.html',{})
