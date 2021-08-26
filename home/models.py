from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    date = models.DateField()


class Login(models.Model):
    emailid = models.EmailField()
    password= models.CharField(max_length=500)
    date = models.DateField()