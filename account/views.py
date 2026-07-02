from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .models import Otp, User
from .forms import LoginForm, OtpLoginForm, OtpForm
from .send_sms import send_sms
from random import  randint
from uuid import uuid4

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None ,'Invalid username or password.')
        return render(request, 'account/login.html', {'form': form})

# login and register
class OtpLoginView(View):

    def get(self, request):
        form = OtpLoginForm()
        return render(request, 'account/auth.html', {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            randcode = randint(1000, 9999)
            send_sms(form.cleaned_data['phone'],randcode)
            token = str(uuid4())
            Otp.objects.create(phone=form.cleaned_data['phone'], random_code=randcode, token=token)
            return redirect(reverse('account:check')+ f'?token={token}')
        else:
            form.add_error(None ,'Invalid phone.')

        return render(request, 'account/auth.html', {'form': form})


class CheckOtpView(View):

    def get(self, request):
        form = OtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = Otp.objects.filter(token=token, random_code=form.cleaned_data['random_code']).first()
            if otp is None:
                form.add_error(None ,'Invalid OTP.')
            else:
                user, _ = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect('/')
        return render(request, 'account/check_otp.html', {'form': form})



