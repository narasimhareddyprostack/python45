from django.shortcuts import render

# Create your views here.


def getindex(request):
    return render(request, 'index.html')


def getabout(request):
    return render(request, 'about.html')


def getservice(request):
    return render(request, 'service.html')


def getcontact(request):
    return render(request, 'contact.html')
