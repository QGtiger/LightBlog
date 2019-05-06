from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Comment_reply)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_reply']