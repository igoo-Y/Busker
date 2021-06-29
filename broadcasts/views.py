from django.shortcuts import render
from .models import Broadcast

def home(request):
    # broadcasts = Broadcast.objects.all()
    return render(request, "broadcasts/broadcasts_list.html")


def broadcast(request):
    pass