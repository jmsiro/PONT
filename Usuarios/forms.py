from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#El Formulario utiliza el modelo de Usuario de Django, el nombre de los campos son los definidos alli (Ver documentación Django).
class UsuarioForm(UserCreationForm):

    username = forms.CharField(label="Nomrbe de Usuario")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    groups = forms.CharField(label="Grupo")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']