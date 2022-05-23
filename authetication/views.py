import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request,"Your account has been created successfully")

        return redirect('signin')
    return render(request,"authentication/signup.html")


def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd = request.POST.get('pass1')

        user = authenticate(username=username,password=pwd)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    pass