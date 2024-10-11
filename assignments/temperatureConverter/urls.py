from django.urls import path
from temperatureConverter import views

urlpatterns = [
    path("", views.tempconv, name = "convert_temperature")
]