# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        # username=request.POST['username']
        username = request.POST.get('username')
        f_name = request.POST.get('name1')
        l_name = request.POST.get('name2')
        address = request.POST.get('address')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = f_name
        myuser.last_name = l_name

        myuser.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            firstname = user.first_name
            return render(request, 'authentication/index.html', {'name': firstname})
        else:
            messages.error(request, "Bad credetials!")

            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
