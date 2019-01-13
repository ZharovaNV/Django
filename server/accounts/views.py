from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .forms import DefaultLoginForm


def login_view(request):
    success_url = reverse_lazy('main:index')
    form = DefaultLoginForm()

    if request.method == 'POST':
        form = DefaultLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            usr = authenticate(
                username=username,
                password=password
            )

            if usr and usr.is_active:
                login(request, usr)

                return redirect(success_url)

    return render(
        request,
        'accounts/login.html',
        {
            'form': form
        }
    )
