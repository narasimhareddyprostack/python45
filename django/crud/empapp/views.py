from django.shortcuts import render, redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee
# Create your views here.


def createempview(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect("/read")
            except:
                pass

    else:
        empform = EmployeeForm()

    return render(request, 'create.html', {'empform': empform})


def displayempview(request):
    emp_list = Employee.objects.all()
    return render(request, 'display.html', {'emp_list': emp_list})


def upateempview(request):
    pass


def deletempview(request, id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()
    return redirect('/read')
