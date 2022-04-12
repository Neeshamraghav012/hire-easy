
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from resume.forms import RegisterForm, LoginForm


#### USER REGISTRATION <<<< ==============================================================================>>>>
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            pass1 = form.cleaned_data['pass1']
            pass2 = form.cleaned_data['pass2']
            username = form.cleaned_data['username']

            try:

                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {"msg": "Username already exists"})

            except User.DoesNotExist:

                if pass1 == pass2:

                    user = User.objects.create_user(username = username, password = pass1)
                    user.save()

                    login(request, user)
                    return redirect("/")

                else:
                    messages.success(request, "Password didn't match.")

    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {"form": form})



def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password = password)

            if user is not None:

                login(request, user)

                return redirect("/")

            else:

                messages.info(request, "Invalid Credentials.")
                return render(request, "accounts/login.html", {"form": LoginForm()})

    else:

        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

@login_required
def logout_view(request):

    logout(request)
    messages.success(request, "logout successfuly")
    return redirect("/")
