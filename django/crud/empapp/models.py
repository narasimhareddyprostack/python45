from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=32)
    ename = models.CharField(max_length=32)
    esal = models.IntegerField()
    eemail = models.EmailField()
    # eimage= models.ImageField()

    class Meta:
        db_table = "employee"


# default table name is : empapp_employee
#
