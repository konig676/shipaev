from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(Shift)
admin.site.register(OrderUserList)
admin.site.register(UserList)