from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/header')
        
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
        
    else:
        return render(request,'login.html')


def signout(request):
    auth.logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')