from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Student(models.Model):
    sname = models.CharField(max_length=100)
    psw = models.CharField(max_length=100)

class Teacher(models.Model):
    tname= models.CharField(max_length=100)
    psw= models.CharField(max_length=100)
    department=models.CharField(max_length=100,default='')

class Fileinfo(models.Model):
    format= models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    uid=models.IntegerField()

class Content(models.Model):
    stufileid=models.IntegerField(null=True)
    stuid=models.IntegerField()
    requirement= models.CharField(max_length=100)
    teafileid= models.IntegerField(null=True)
    teaid=models.IntegerField()
    feedback = models.CharField(max_length=100,null=True)
