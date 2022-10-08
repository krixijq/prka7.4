from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationFrom, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
