from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Staff)
admin.site.register(requests)
admin.site.register(tag)
admin.site.register(orders)
