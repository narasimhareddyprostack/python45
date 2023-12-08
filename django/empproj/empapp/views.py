from django.shortcuts import render
from empapp.forms import EmployeeForm, UserForm
from empapp.models import Employee, User
# Create your views here.


def gethomepage(request):
    return render(request, 'home.html')


def getempregpage(request):
    empform = EmployeeForm()
    return render(request, 'emp.html', {'empform': empform})


""" def getsuccesspage(request):
    if request.method == "POST":
        eid = request.POST['eid']
        ename = request.POST['ename']
        eloc = request.POST['eloc']
        email = request.POST.get('email')
        print(eid, ename, eloc, email)
        empdata = Employee(eid=eid, ename=ename, eloc=eloc, email=email)
        empdata.save()

    return render(request, 'success.html')
 """


def getsuccesspage(request):
    if request.method == "POST":
        empdata = EmployeeForm(request.POST)
        if empdata.is_valid():
            empdata.save()

    return render(request, 'success.html')


def getuserreg(request):
    userform = UserForm()
    return render(request, 'user.html', {'userform': userform})


def getusersuccesspage(request):
    if request.method == 'POST':
        # userdata = UserForm(request.POST)
        uname = request.POST['uname']
        uloc = request.POST.get('uloc')
        userdata = User(uname=uname, uloc=uloc)
        userdata.save()
    return render(request, 'success.html')
