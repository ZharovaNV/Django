from django import forms


class LoginForm(forms.Form):
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