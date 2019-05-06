from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'company', 'profession', 'address', 'aboutme', 'photo']
    list_filter = ('school', )
    search_fields = ['user__username', 'school',]
