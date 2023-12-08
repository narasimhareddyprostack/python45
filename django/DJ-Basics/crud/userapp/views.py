from django.shortcuts import render
from userapp.forms import UserForm
from userapp.forms import EmployeeForm
from userapp.models import Employee
# Create your views here.


def gethomepage(request):
    return render(request, 'home.html')


def getnewuserpage(request):
    if request.method == "POST":
        uid = request.POST['uid']
        uname = request.POST['uname']
        uloc = request.POST['uloc']
        uemail = request.POST['uemail']
        userform = UserForm(uid=uid, uname=uname, uloc=uloc, uemail=uemail)
        print(uid, uname)
        userform.save()

    form = UserForm()
    # myform = {'form': form}
    # prepare resonse
    # return render(request, 'user.html', context=myform)
    return render(request, 'user.html', {'form': form})


def getnewemppage(request):
    form = EmployeeForm()
    return render(request, 'emp.html', {'empform': form})


def saveemp(request):
    if request.method == "POST":
        emp = Employee(request.POST)
        emp.save()
    return render(request, 'home.html')
