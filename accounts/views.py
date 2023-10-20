from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm

# def login(request):
#     return render(request, 'accounts/login.html', {})

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})


    def post(self, request):
        number_of_errors = 0
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'اطلاعات کاربر نامعتبر: تلفن یا رمز عبور اشتباه است')
            # form.add_error('password', f'something wrong')
        return render(request, 'accounts/login.html', {'form': form})

