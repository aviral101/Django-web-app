from django.shortcuts import render,redirect,reverse
from generalzone.models import CustomerInfo,LoginInfo
import datetime
from . models import Complain,Question,Answer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Knowledgebase,Notification
from django.db.models import Q

# Create your views here.
def userhome(request):
    try:   #in case we try to login with userid=null(gets deleted after logout) python gives KeyError
        if request.session['userid']:
            email=request.session.get('userid')
            n=CustomerInfo.objects.get(emailaddress=email)
            name=n.name
            q=Question.objects.all()
            nf=Notification.objects.all()
            return render(request,'userhome.html',{'name':name,'nf':nf,'q':q})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def discussion(request):
    try:
        if request.session['userid']:
            quest=Question.objects.all()
            return render(request,'discussion.html',{'quest':quest})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def searchsolution(request):
    try:
        if request.session['userid']:
            name=request.session.get('userid')
            return render(request,'searchsolution.html',{'name':name})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def complainlog(request):
    try:
        if request.session['userid']:
            name=request.session.get('userid')
            return render(request,'complainlog.html',{'name':name})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def changepassword(request):
    try:
        if request.session['userid']:
            name=request.session.get('userid')
            return render(request,'changepassword.html',{'name':name})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['userid']
        return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def savecomplain(request):
    try:
        if request.session['userid']:
            emailaddress=request.session.get('userid')
            customer=CustomerInfo.objects.get(emailaddress=emailaddress)
            name=customer.name
            gender=customer.gender
            address=customer.address
            contactno=customer.contactno
            subject=request.POST['subject']
            complaintext=request.POST['complaintext']
            complaindate=datetime.datetime.now().strftime('%Y/%m/%d')
            com=Complain(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,subject=subject,complaintext=complaintext,complaindate=complaindate)
            com.save()
            messages.success(request,'Complain Lodged Successfully')
            return redirect('userzone:userhome')
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def changepwd(request):
    try:
        if request.session['userid']:
            userid=request.session.get('userid')
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            try:
                user=LoginInfo.objects.get(userid=userid,password=oldpassword)
                if user is not None:
                    li=LoginInfo(password=newpassword,userid=userid,usertype='customer')
                    li.save()
                    messages.success(request,'Password Changed Successfully')
                    return redirect('userzone:changepassword')
            except ObjectDoesNotExist:
                messages.warning(request,'Incorrect Password')
                return redirect('userzone:changepassword')
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def postquestion(request):
    try:
        if request.session['userid']:
            emailaddress=request.session.get('userid')
            customer=CustomerInfo.objects.get(emailaddress=emailaddress)
            name=customer.name
            questiontext=request.POST['questiontext']
            posteddate=datetime.datetime.now().strftime('%d/%m/%Y')
            q=Question(questiontext=questiontext,askedby=name,posteddate=posteddate)
            q.save()
            return redirect('userzone:discussion')
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def answer(request,qid):
    try:
        if request.session['userid']:
            return render(request,'answer.html',{'qid':qid})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def postanswer(request):
    try:
        if request.session['userid']:
            emailaddress=request.session.get('userid')
            customer = CustomerInfo.objects.get(emailaddress=emailaddress)
            answeredby=customer.name
            qid=request.POST['qid']
            answertext=request.POST['answertext']
            answereddate=datetime.datetime.now().strftime('%d/%m/%Y')
            a=Answer(answertext=answertext,answeredby=answeredby,qid=qid,answereddate=answereddate)
            a.save()
            ans=Answer.objects.filter(qid=qid)
            return render(request,'viewanswer.html',{'ans':ans})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def viewanswer(request,qid):
    try:
        if request.session['userid']:
            quest=Question.objects.get(qid=qid)
            ans=Answer.objects.filter(qid=qid)
            return render(request,'viewanswer.html',{'ans':ans,'quest':quest})
        else:
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')
def search(request):
    try:
        if request.session['userid']:
            searchtext=request.POST['searchtext']
            kw=Knowledgebase.objects.filter(Q(problemid=searchtext) | Q(problemtext=searchtext))
            return render(request,'searchsolution.html',{'kw':kw})
    except KeyError:
        return render(request,'login.html')