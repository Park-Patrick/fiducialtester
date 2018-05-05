from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. I don't know what I'm doing.")
