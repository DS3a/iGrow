from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view_sensor_vals/', views.view_sensor_vals, name="view"),
    path('atmosphere_regulation/', views.send_vals, name="atmosphere_regulation"),
    path('sensor_vals_input/', views.get_sensor_vals, name="sensor_values"),
]
