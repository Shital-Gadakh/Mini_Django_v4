from django.shortcuts import render
from django.http import HttpResponse

from jobs.models import Portal


# Create your views here.


def welcome(request):
    return HttpResponse("welcome page can be success")


def portal_details(request):
    objs = Portal.objects.all()
    portals = []
    for obj in objs:
        portals.append(f"{obj.name}")

    final = "======".join(portals)
    return HttpResponse(f"<p> {final}</p>")


