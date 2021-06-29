from django.shortcuts import render
from .models import Broadcast


def broadcasts_list(request):
    return render(request, "broadcasts/broadcasts_list.html")


def broadcast(request):
    context = {}

    return render(request, "broadcasts/main.html", context=context)
