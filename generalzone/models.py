from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)
class CustomerInfo(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    nationality=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    connectdate = models.CharField(max_length=20)
class LoginInfo(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)