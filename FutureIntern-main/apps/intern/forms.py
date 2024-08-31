from django import forms

from apps.intern.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets={
        'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }
