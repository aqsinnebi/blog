from django.contrib import admin

# Register your models here.
from . models import Test,Comment


admin.site.register(Test)
admin.site.register(Comment)