from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'column', 'created']
    list_filter = ('user',)
    search_fields = ('user__username', 'column',)


@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'column', 'created', 'updated']
    list_filter = ('author__username', 'title', )
    search_fields = ('id', 'author__username', 'title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'commentator', 'body', 'created', 'is_read']
    list_filter = ('commentator__username', 'article__title',)
    search_fields = ['id', 'commentator__username', 'article__title']
