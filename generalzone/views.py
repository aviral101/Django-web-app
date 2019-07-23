from django.shortcuts import render,redirect,reverse
from . models import Enquiry,CustomerInfo,LoginInfo
import datetime
from django.contrib import messages
from . import smssender
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification

# Create your views here.

def index(request):
    nf=Notification.objects.all()
    return render(request,'index.html',{'nf':nf})
def about(request):
    nf=Notification.objects.all()
    return render(request,'about.html',{'nf':nf})
def registration(request):
    nf=Notification.objects.all()
    return render(request,'registration.html',{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,'login.html',{'nf':nf})
def enquiry(request):
    nf=Notification.objects.all()
    return render(request,'enquiry.html',{'nf':nf})
def saveenquiry(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.now().strftime('%Y/%m/%d')
    en=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    en.save()
    #smssender.sendsms(contactno,'Thanks for enquiry. We will contact you soon '
                               # '- Team HR,CPO')
    messages.success(request,'Enquiry Successfully Saved.')     #This will return the message to the page redirected
    return redirect('index')
def custreg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    nationality=request.POST['nationality']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    password=request.POST['password']
    connectdate=datetime.datetime.now().strftime('%Y/%m/%d')
    usertype='customer'

    if CustomerInfo.objects.filter(emailaddress=emailaddress).exists():
        messages.warning(request, 'User already registered.')
    else:
        ci = CustomerInfo(name=name, gender=gender, address=address, nationality=nationality, contactno=contactno,
                          emailaddress=emailaddress, password=password, connectdate=connectdate)
        li = LoginInfo(userid=emailaddress, password=password, usertype=usertype)
        ci.save()
        li.save()
        messages.success(request, 'Registration Successful.')
    return redirect('registration')
def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        v=LoginInfo.objects.get(userid=userid,password=password)
        if v is not None:
            usertype=v.usertype
            if usertype=='customer':
                request.session['userid']=userid               #used to pass value of userid to views.py file of new app i.e userzone
                return redirect(reverse('userzone:userhome'))  #reverse is used if we want to access template of another app
            elif usertype=='admin':
                request.session['adminid']=userid
                return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        messages.warning(request,'Incorrect User Id or Password')
        return redirect('login')
