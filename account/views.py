from django.shortcuts import render, redirect
from django.urls import reverse
# from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
        authenticate,
        login as auth_login,
        logout as auth_logout,
    )
from .models import Profile
from .forms import (
        AuthForm,
        SignupForm,
        ProfileForm,
    )
# Create your views here.


def login(request):
    form = AuthForm(request, request.POST or None)
    next_url = reverse('core:main_page')
    if request.user.is_authenticated:
        return redirect(next_url)
    else:
        if request.method == 'POST' and form.is_valid():
            auth_login(request, form.get_user())
            # next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
            # next_url = settings.LOGIN_REDIRECT_URL
            return redirect(next_url)
        ctx = {
            'form': form,
        }
        return render(request, 'account/login.html', ctx)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('core:main_page')


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('account:login')
    ctx = {
        'form': form,
    }
    return render(request, 'account/signup.html', ctx)


@login_required
def read_profile(request):
    profile = Profile.objects.get(user__pk=request.user.pk)
    return render(request, 'account/read_profile.html', {'profile': profile, })


@login_required
def update_profile(request):
    try:
        profile_form = ProfileForm(request.POST or None, instance=request.user.profile)
    except:  # 예외처리 에러 몰라서 작성 안함
        profile_form = ProfileForm(request.POST or None)
    if request.method == 'POST' and profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('core:main_page')
    ctx = {
        'profile_form': profile_form,
    }
    return render(request, 'profile_edit.html', ctx)
