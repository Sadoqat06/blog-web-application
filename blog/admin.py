from django.contrib import admin
from .models import Author, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('author_name', 'content')



admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)