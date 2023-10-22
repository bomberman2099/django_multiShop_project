from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOTPForm
import ghasedakpack
from random import randint
from uuid import uuid4
from .models import OTP, User

sms = ghasedakpack.Ghasedak("f37be99bbfd2da5b474c9303339e6eda55f9feaedad21f211fd8c355c5320bb0")


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


class UserRegister(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            randomCode = randint(1000,9999)
            cd = form.cleaned_data
            sms.verification({'receptor': cd['phone'], 'type': '1', 'template': 'Your Template', 'param1': randomCode})
            token = str(uuid4())
            OTP.objects.create(phone=cd['phone'], code=randomCode, token=token)
            print(randomCode, token)
            return redirect(reverse('accounts:user_check_OTP_register') + f'?token={token}')

        else:
            form.add_error('phone', 'اطلاعات نا معتبر')
        return render(request, 'accounts/login.html', {'form': form})



class Check_User_OTP(View):
    def get(self, request):
        form = CheckOTPForm()
        return render(request, 'accounts/check_OTP.html', {"form": form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOTPForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #User inputs
            if OTP.objects.filter(code=cd['code'], token=token).exists():
                otp = OTP.objects.get(token=token)
                user = User.objects.get(phone=otp.phone)
                login(request, user)
                return redirect('/')
        else:
            form.add_error('phone', 'اطلاعات نا معتبر')
        return render(request, 'accounts/check_OTP.html', {'form': form})
