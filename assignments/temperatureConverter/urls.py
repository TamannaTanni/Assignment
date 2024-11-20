from django.urls import path
from temperatureConverter import views

app_name = 'temperatureConverter'

urlpatterns = [
    path("", views.tempconv, name = "convert_temperature")
]