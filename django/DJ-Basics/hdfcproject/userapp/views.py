from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def getindexpage(request):
    msg = '<h2>Index Page</h2>'
    return HttpResponse(msg)


def getaboutpage(request):
    return HttpResponse('About Page')


def getservicepage(request):
    return HttpResponse('Service Page')


def getcontactpage(request):
    return HttpResponse('Contact Page')


def getloginpage(request):
    return HttpResponse('Login Page')
