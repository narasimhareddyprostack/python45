from django import forms
from empapp.models import Employee, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['uname', 'uloc']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'eloc', 'email']


""" class EmployeeForm(forms.Form):
    eid = forms.IntegerField(label="Id")
    ename = forms.CharField(label="Name")
    eloc = forms.CharField(label="Location")
    email = forms.CharField(label="Email") """
