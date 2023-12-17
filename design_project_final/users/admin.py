from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Teacher

class Teacher(admin.StackedInline):
    model = Teacher
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (Teacher,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

