from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form=CustomUserChangeForm
    model = CustomUserChangeForm
    list_display = ['email', 'username', 'name']

admin.site.register(CustomUser, CustomerUserAdmin)