from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=32)
    uloc = models.CharField(max_length=32)
    uemail = models.CharField(max_length=32)
