# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'rol', 'telefono', 'direccion')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'rol', 'telefono', 'direccion')

