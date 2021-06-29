from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("", views.broadcast, name="broadcast"),
]
