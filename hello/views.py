from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def person(request):
    return HttpResponse("Hello, Person")


def vlad(request):
    return HttpResponse("Hello, Vlad")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
