from django import forms
from .models import Accountuser


class LoginForm(forms.ModelForm):
    class Meta:
        model = Accountuser
        fields = ['username', 'password']
        widgets = {
            'password': forms.widgets.PasswordInput(
                attrs={
                    'class': 'field field-password'
                }
            )
        }


class  DefaultLoginForm(forms.Form):
    username = forms.CharField(
        label='login',
        max_length=150,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'field field-password'
            }
        )
    )
    password = forms.CharField(
        max_length=72,
        widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'field field-password'
            }
        )
    )