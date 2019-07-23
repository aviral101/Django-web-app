from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^enquiries',views.enquiries,name='enquiries'),
    url(r'^complains',views.complains,name='complains'),
    url(r'^customerinfo',views.customerinfo,name='customerinfo'),
    url(r'^knowledgebase',views.knowledgebase,name='knowledgebase'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^addnotification',views.addnotification,name='addnotification'),
    url(r'^deletenotification/(?P<id>\d+)$',views.deletenotification,name='deletenotification'),
    url(r'^deleteenquiries/(?P<id>\d+)$',views.deleteenquiries,name='deleteenquiries'),
    url(r'^deletecomplain/(?P<id>\d+)$',views.deletecomplain,name='deletecomplain'),
    url(r'^deletecustomerinfo/(?P<emailaddress>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deletecustomerinfo,name='deletecustomerinfo'),
    url(r'^saveknowledgebase',views.saveknowledgebase,name='saveknowledgebase')
]