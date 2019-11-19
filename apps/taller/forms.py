from django import forms
from apps.taller.models import Tecnico, Especializacion, User, Cliente

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'id':'nombre', 'name':'nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'id':'apellido', 'name':'apellido'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'id':'usuario', 'name':'usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'correo', 'name':'correo'}),
            'especializacion': forms.SelectMultiple(),
            'password': forms.TextInput(attrs={'class':'form-control', 'id':'password', 'name':'password'}),
            'password_2': forms.TextInput(attrs={'class':'form-control', 'id':'password_2', 'name':'password_2'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'id':'telefono', 'name':'telefono'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'id':'direccion', 'name':'direccion'}),
            'activo': True,
            'staff': True,
            'rol': '1',
        }
