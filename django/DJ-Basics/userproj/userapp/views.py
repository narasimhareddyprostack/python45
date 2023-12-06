from django.shortcuts import render
from userapp.models import User
# Create your views here.


def getuserdata(request):
    user_list = User.objects.all()
    return render(request, 'user.html', context={'user_list': user_list})


def gethomepage(request):
    return render(request, 'home.html')
