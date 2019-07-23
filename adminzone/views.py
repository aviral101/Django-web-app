from django.shortcuts import render,redirect
import datetime
from generalzone.models import Enquiry,CustomerInfo,LoginInfo
from userzone.models import Complain
from django.contrib import messages
from . models import Knowledgebase,Notification


# Create your views here.
def adminhome(request):
    try:   #in case we try to login with adminid=null(gets deleted after logout) python gives KeyError
        if request.session['adminid']:
            name = request.session.get('adminid')
            noti=Notification.objects.all()
            return render(request,'adminhome.html',{'name':name,'noti':noti})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def enquiries(request):
    try:
        if request.session['adminid']:
            name = request.session.get('adminid')
            enq=Enquiry.objects.all()
            return render(request,'enquiries.html',{'name':name,'enq':enq})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def complains(request):
    try:
        if request.session['adminid']:
            name = request.session.get('adminid')
            comp=Complain.objects.all()
            return render(request,'complains.html',{'name':name,'comp':comp})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def customerinfo(request):
    try:
        if request.session['adminid']:
            name = request.session.get('adminid')
            cust=CustomerInfo.objects.all()
            return render(request,'customerinfo.html',{'name':name,'cust':cust})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def knowledgebase(request):
    try:
        if request.session['adminid']:
            name=request.session.get('adminid')
            return render(request,'knowledgebase.html',{'name':name})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['adminid']
        return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def addnotification(request):
    try:
        if request.session['adminid']:
            notificationtext=request.POST['notificationtext']
            posteddate=datetime.datetime.now().strftime('%d/%m/%Y')
            n=Notification(notificationtext=notificationtext,posteddate=posteddate)
            n.save()
            return redirect('adminzone:adminhome')
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def deletenotification(request,id):
    try:
        if request.session['adminid']:
            e=Notification.objects.get(id=id)
            e.delete()
            return redirect('adminzone:adminhome')
    except KeyError:
        return render(request,'login.html')
def deleteenquiries(request,id):
    try:
        if request.session['adminid']:
            e=Enquiry.objects.get(id=id)
            e.delete()
            return redirect('adminzone:enquiries')
    except KeyError:
        return render(request,'login.html')
def deletecomplain(request,id):
    try:
        if request.session['adminid']:
            c=Complain.objects.get(id=id)
            c.delete()
            return redirect('adminzone:complains')
    except KeyError:
        return render(request,'login.html')
def deletecustomerinfo(request,emailaddress):
    try:
        if request.session['adminid']:
            c=CustomerInfo.objects.get(emailaddress=emailaddress)
            l=LoginInfo.objects.get(userid=emailaddress)
            c.delete()
            l.delete()
            return redirect('adminzone:customerinfo')
    except KeyError:
        return render(request,'login.html')
def saveknowledgebase(request):
    try:
        if request.session['adminid']:
            problemid=request.POST['problemid']
            problemtext=request.POST['problemtext']
            solutiontext=request.POST['solutiontext']
            posteddate=datetime.datetime.now().strftime('%d/%m/%Y')
            kw=Knowledgebase(problemid=problemid,problemtext=problemtext,solutiontext=solutiontext,posteddate=posteddate)
            kw.save()
            return redirect('adminzone:knowledgebase')
    except KeyError:
        return render(request,'login.html')