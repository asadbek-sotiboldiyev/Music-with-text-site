from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .functions import check_email

def LoginPage(request):
    context={}
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            context['error']="Ma'lumotlar xato"
    return render(request, 'registration/login.html',context)

def SignUpPage(request):
    context={}
    if request.method=='POST':
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if check_email(email):
                new_user=User.objects.create_user(email=email,username=email,password=password1)
                new_user.save()
                return redirect('login')
            else:
                context['error']='Email band'
        else:
            context['error']='Parollar mos emas'
    return render(request,'registration/signup.html',context)

def Logout(request):
    logout(request)
    return redirect('home_page')