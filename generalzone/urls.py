from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^login',views.login,name='login'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^saveenquiry',views.saveenquiry,name='saveenquiry'),
    url(r'^custreg',views.custreg,name='custreg'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
]
admin.site.site_title = "CPO Admin"
admin.site.site_header = "CPO Administration"