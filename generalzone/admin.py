from django.contrib import admin
from . models import Enquiry,CustomerInfo,LoginInfo

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(CustomerInfo)
admin.site.register(LoginInfo)