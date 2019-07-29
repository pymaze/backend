from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomerUser
        fields=UserChangeForm.Meta.fields