

from django.http import HttpResponse
from django.shortcuts import render


def hello(request,nom):
    return HttpResponse(f"Hello World {nom}")

def hellohtml(request):
    data = {
        "nom":"Rakoto",
        "age":32,
        "taille":1.75,
        "genre":"Homme",
    }
    return render(request, "hello.html", data)