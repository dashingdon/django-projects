from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.index , name='index'),
    path('contact.html', views.contact , name='contact'),
]
