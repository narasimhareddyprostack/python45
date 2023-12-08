from django import forms
from userapp.models import Employee


class UserForm(forms.Form):
    uid = forms.IntegerField(label="User Id")
    uname = forms.CharField(label="Name")
    uloc = forms.CharField(label="Location", required=False)
    uemail = forms.CharField(label="Email")


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee
        # fields = "__all__"
        fields = ['eid', 'ename', 'esal']
