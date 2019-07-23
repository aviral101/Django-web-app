from django.contrib import admin
from . models import Complain,Question,Answer

# Register your models here.
admin.site.register(Complain)
admin.site.register(Question)
admin.site.register(Answer)