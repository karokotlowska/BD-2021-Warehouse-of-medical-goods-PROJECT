from django import forms



class loginForm(forms.Form):
    login = forms.CharField(label = 'login', max_length=100)
    password = forms.CharField(label = 'haslo', max_length=100, widget=forms.PasswordInput())