from django.contrib import admin
from .models import *
# Register your models here.

#검색기능 구현
class TitleAdmin(admin.ModelAdmin):
    search_fields =['title']

admin.site.register(Blog, TitleAdmin)