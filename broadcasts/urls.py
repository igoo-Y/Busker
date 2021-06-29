from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("lists/", views.broadcasts_list, name="broadcasts_list"),
    path("", views.broadcast, name="broadcast"),
]
