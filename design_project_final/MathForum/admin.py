from django.contrib import admin
from .models import Category, Post, Comment
from django.contrib.auth.admin import UserAdmin

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

