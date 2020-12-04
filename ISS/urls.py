from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns= [
    path('locations', views.sendISSLocation, name="sendISSLocation"),
    path('messages', csrf_exempt(views.directMessage), name="directMessage")
]