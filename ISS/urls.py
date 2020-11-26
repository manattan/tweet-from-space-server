from django.urls import path
from . import views

urlpatterns= [
    path('locations', views.sendISSLocation, name="sendISSLocation")
]