from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Ingrese el usuario:')
    email = forms.EmailField(label='Ingrese su correo:')
    password = forms.CharField(label='Ingrese su clave:',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme su clave:', widget=forms.PasswordInput)

    def clean_password2(self):
        print "Entro"
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            print "que pasa"
            raise forms.ValidationError("La clave debe ser la misma! ")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("Este usuario ya existe!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("Este email ya esta registrado!")
        return email
